"""Generate a reproducible synthetic transaction CSV for offline experiments."""
from pathlib import Path
import numpy as np
import pandas as pd

def generate(path=None, rows=3000, seed=42):
    rng=np.random.default_rng(seed)
    senders=rng.integers(1,201,rows); receivers=rng.integers(1,201,rows)
    amounts=np.round(rng.lognormal(4,1,rows),2); hours=rng.integers(0,24,rows)
    labels=((amounts>1800)|((hours<5)&(amounts>450))).astype(int)
    df=pd.DataFrame({"transaction_id":[f"SYN-{i:06d}" for i in range(rows)],"sender_id":[f"ACCT-{x:04d}" for x in senders],"receiver_id":[f"ACCT-{x:04d}" for x in receivers],"amount":amounts,"hour":hours,"synthetic_label":labels})
    target=Path(path) if path else Path(__file__).with_name("transactions.csv")
    df.to_csv(target,index=False); return target

if __name__ == "__main__": print(generate())
