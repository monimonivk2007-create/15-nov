import networkx as nx
from sqlalchemy import func
from ..models import Transaction, Account

def account_network(db, account_id):
    rows = db.query(Transaction).filter((Transaction.sender_id == account_id) | (Transaction.receiver_id == account_id)).all()
    graph = nx.DiGraph()
    for tx in rows:
        graph.add_edge(tx.sender_id, tx.receiver_id, amount=tx.amount, transaction_id=tx.id)
    return {"nodes": [{"id": n, "degree": int(graph.degree(n))} for n in graph.nodes], "edges": [{"source": a, "target": b, "amount": d["amount"]} for a,b,d in graph.edges(data=True)]}

def refresh_mule_flags(db):
    for account in db.query(Account).all():
        incoming = db.query(func.count(Transaction.id)).filter(Transaction.receiver_id == account.id).scalar() or 0
        outgoing = db.query(func.count(Transaction.id)).filter(Transaction.sender_id == account.id).scalar() or 0
        in_amt = db.query(func.coalesce(func.sum(Transaction.amount), 0)).filter(Transaction.receiver_id == account.id).scalar() or 0
        out_amt = db.query(func.coalesce(func.sum(Transaction.amount), 0)).filter(Transaction.sender_id == account.id).scalar() or 0
        # Heuristic candidate only: many incoming transfers followed by substantial outflow.
        account.is_potential_mule = int(incoming >= 5 and outgoing >= 4 and out_amt >= in_amt * .55)
        account.risk_score = max(account.risk_score or 0, 65 if account.is_potential_mule else 0)
