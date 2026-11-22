from datetime import datetime, timezone, timedelta
from uuid import uuid4
import os, random
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc
from .database import Base, engine, get_db, SessionLocal
from .models import Account, Transaction, FraudAlert, ModelLog
from .schemas import TransactionCreate
from .services.fraud_detector import score, load_models
from .services.risk_scoring import risk_level
from .services.mule_detector import account_network, refresh_mule_flags

app = FastAPI(title="FINTRUST AI", description="Synthetic transaction fraud and mule-risk assessment prototype")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

def init_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        load_models()
        if db.query(Transaction).count(): return
        rng = random.Random(42)
        ids = [f"ACCT-{i:04d}" for i in range(1, 81)]
        db.add_all([Account(id=x) for x in ids]); db.flush()
        now = datetime.now(timezone.utc)
        for i in range(int(os.getenv("SEED_TRANSACTIONS", "300"))):
            sender, receiver = rng.sample(ids, 2); amount = round(rng.lognormvariate(4.0, 1.0), 2)
            if i % 35 == 0: amount = round(rng.uniform(2200, 5500), 2)
            ts = now - timedelta(minutes=rng.randint(0, 60*24*14))
            p,risk,label,reason = score(amount, rng.randint(0,20), rng.randint(0,20), ts.hour)
            tx = Transaction(id=f"TX-{uuid4().hex[:12].upper()}",sender_id=sender,receiver_id=receiver,amount=amount,timestamp=ts,status="completed",fraud_probability=round(p*100,1),risk_score=risk,classification=label,detection_reason=reason)
            db.add(tx); db.flush()
            if risk >= 31:
                db.add(FraudAlert(id=f"ALT-{uuid4().hex[:10].upper()}",transaction_id=tx.id,account_id=sender,amount=amount,fraud_probability=round(p*100,1),risk_level=risk_level(risk),detection_reason=reason,timestamp=ts))
                db.add(ModelLog(transaction_id=tx.id,fraud_probability=p,classification=label))
        db.commit(); refresh_mule_flags(db); db.commit()
    finally: db.close()

@app.on_event("startup")
def startup(): init_data()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("frontend/templates/dashboard.html", encoding="utf-8") as f: return f.read()

@app.get("/transactions")
def transactions(search: str|None=None, risk: str|None=None, sort: str="date", limit: int=Query(100,ge=1,le=500), offset: int=0, db: Session=Depends(get_db)):
    q=db.query(Transaction)
    if search: q=q.filter(or_(Transaction.id.contains(search),Transaction.sender_id.contains(search),Transaction.receiver_id.contains(search)))
    if risk: q=q.filter(Transaction.classification.ilike(f"%{risk}%"))
    q=q.order_by(Transaction.amount if sort=="amount" else desc(Transaction.timestamp)).offset(offset).limit(limit)
    return [tx_dict(x) for x in q.all()]

def tx_dict(x):
    return {"id":x.id,"sender_id":x.sender_id,"receiver_id":x.receiver_id,"amount":x.amount,"timestamp":x.timestamp,"status":x.status,"fraud_probability":x.fraud_probability,"risk_score":x.risk_score,"risk_level":risk_level(x.risk_score),"classification":x.classification,"detection_reason":x.detection_reason}

@app.post("/transactions")
def add_transaction(payload: TransactionCreate, db: Session=Depends(get_db)):
    if payload.sender_id==payload.receiver_id: raise HTTPException(400,"Sender and receiver must differ")
    for aid in (payload.sender_id,payload.receiver_id):
        if not db.get(Account,aid): db.add(Account(id=aid))
    db.flush()
    sender_count=db.query(Transaction).filter(Transaction.sender_id==payload.sender_id).count()
    receiver_count=db.query(Transaction).filter(Transaction.receiver_id==payload.receiver_id).count()
    ts=payload.timestamp or datetime.now(timezone.utc)
    p,risk,label,reason=score(payload.amount,sender_count,receiver_count,ts.hour)
    tx=Transaction(id=f"TX-{uuid4().hex[:12].upper()}",sender_id=payload.sender_id,receiver_id=payload.receiver_id,amount=payload.amount,timestamp=ts,status="completed",fraud_probability=round(p*100,1),risk_score=risk,classification=label,detection_reason=reason)
    db.add(tx); db.flush()
    if risk>=31: db.add(FraudAlert(id=f"ALT-{uuid4().hex[:10].upper()}",transaction_id=tx.id,account_id=payload.sender_id,amount=payload.amount,fraud_probability=round(p*100,1),risk_level=risk_level(risk),detection_reason=reason))
    db.add(ModelLog(transaction_id=tx.id,fraud_probability=p,classification=label)); db.commit(); db.refresh(tx)
    refresh_mule_flags(db); db.commit()
    return tx_dict(tx)

@app.get("/transactions/{transaction_id}")
def transaction_detail(transaction_id: str, db: Session=Depends(get_db)):
    tx=db.get(Transaction,transaction_id)
    if not tx: raise HTTPException(404,"Transaction not found")
    return tx_dict(tx)

@app.get("/fraud-alerts")
def alerts(risk: str|None=None, db: Session=Depends(get_db)):
    q=db.query(FraudAlert)
    if risk: q=q.filter(FraudAlert.risk_level.ilike(risk))
    return [{"id":a.id,"transaction_id":a.transaction_id,"account_id":a.account_id,"amount":a.amount,"fraud_probability":a.fraud_probability,"risk_level":a.risk_level,"detection_reason":a.detection_reason,"timestamp":a.timestamp} for a in q.order_by(desc(FraudAlert.timestamp)).limit(300).all()]

@app.get("/dashboard/summary")
def summary(db: Session=Depends(get_db)):
    txs=db.query(Transaction).all(); accounts=db.query(Account).all()
    groups={"Legitimate Transaction":0,"Suspicious Transaction":0,"Potentially Fraudulent Transaction":0}
    for t in txs: groups[t.classification]=groups.get(t.classification,0)+1
    risk_counts={k:sum(1 for t in txs if risk_level(t.risk_score)==k) for k in ["Low","Medium","High","Critical"]}
    byday={}
    for t in txs:
        day=t.timestamp.date().isoformat(); byday[day]=byday.get(day,0)+1
    top=sorted(accounts,key=lambda a:a.risk_score or 0,reverse=True)[:8]
    return {"total_transactions":len(txs),"legitimate":groups["Legitimate Transaction"],"suspicious":groups["Suspicious Transaction"],"fraudulent":groups["Potentially Fraudulent Transaction"],"potential_mule_accounts":sum(a.is_potential_mule for a in accounts),"flagged_amount":round(sum(t.amount for t in txs if t.risk_score>=31),2),"risk_distribution":risk_counts,"volume_over_time":dict(sorted(byday.items())),"classification_counts":groups,"top_accounts":[{"id":a.id,"risk_score":a.risk_score,"is_potential_mule":bool(a.is_potential_mule)} for a in top]}

@app.get("/accounts")
def accounts(db: Session=Depends(get_db)):
    refresh_mule_flags(db); db.commit()
    return [{"id":a.id,"risk_score":a.risk_score,"is_potential_mule":bool(a.is_potential_mule)} for a in db.query(Account).order_by(desc(Account.risk_score)).all()]

@app.get("/accounts/{account_id}")
def account_detail(account_id: str, db: Session=Depends(get_db)):
    a=db.get(Account,account_id)
    if not a: raise HTTPException(404,"Account not found")
    txs=db.query(Transaction).filter(or_(Transaction.sender_id==account_id,Transaction.receiver_id==account_id)).order_by(desc(Transaction.timestamp)).limit(50).all()
    return {"id":a.id,"risk_score":a.risk_score,"is_potential_mule":bool(a.is_potential_mule),"transactions":[tx_dict(t) for t in txs]}

@app.get("/accounts/{account_id}/network")
def network(account_id: str, db: Session=Depends(get_db)):
    if not db.get(Account,account_id): raise HTTPException(404,"Account not found")
    return account_network(db,account_id)

@app.post("/predict-fraud")
def predict(payload: TransactionCreate, db: Session=Depends(get_db)):
    n1=db.query(Transaction).filter(Transaction.sender_id==payload.sender_id).count(); n2=db.query(Transaction).filter(Transaction.receiver_id==payload.receiver_id).count()
    p,r,l,reason=score(payload.amount,n1,n2,(payload.timestamp or datetime.now(timezone.utc)).hour)
    return {"fraud_probability":round(p*100,1),"risk_score":r,"risk_level":risk_level(r),"classification":l,"detection_reason":reason,"assessment":"Algorithmic assessment of synthetic/demo patterns; not a determination of criminal activity."}

@app.get("/model/performance")
def performance(): return load_models()[2]

