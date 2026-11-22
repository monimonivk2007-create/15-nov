"""Deterministic synthetic-data classifier and anomaly detector."""
from pathlib import Path
import joblib
import numpy as np
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

MODEL_PATH = Path(__file__).resolve().parents[2] / "ml" / "saved_model" / "fraud_models.joblib"
FEATURES = ["amount", "sender_count", "receiver_count", "hour", "account_activity"]

def train_models(seed=42):
    rng = np.random.default_rng(seed)
    n = 5000
    amount = rng.lognormal(3.8, 1.0, n)
    sender_count = rng.poisson(4, n)
    receiver_count = rng.poisson(5, n)
    hour = rng.integers(0, 24, n)
    activity = sender_count + receiver_count
    labels = ((amount > 1800) | ((hour < 5) & (amount > 450)) | ((sender_count > 16) & (receiver_count > 12))).astype(int)
    X = np.column_stack([amount, sender_count, receiver_count, hour, activity])
    X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=.2, random_state=seed, stratify=labels)
    clf = RandomForestClassifier(n_estimators=120, class_weight="balanced", random_state=seed, min_samples_leaf=2)
    clf.fit(X_train, y_train)
    anomaly = IsolationForest(contamination=.03, random_state=seed).fit(X_train)
    pred = clf.predict(X_test)
    metrics = {"accuracy": float(accuracy_score(y_test,pred)), "precision": float(precision_score(y_test,pred,zero_division=0)), "recall": float(recall_score(y_test,pred,zero_division=0)), "f1": float(f1_score(y_test,pred,zero_division=0)), "confusion_matrix": confusion_matrix(y_test,pred).tolist(), "dataset": "synthetic", "note": "Experimental metrics on generated data; not real-world performance."}
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"classifier":clf,"anomaly":anomaly,"metrics":metrics}, MODEL_PATH)
    return clf, anomaly, metrics

_cached = None
def load_models():
    global _cached
    if _cached is not None: return _cached
    if MODEL_PATH.exists():
        try:
            data = joblib.load(MODEL_PATH)
            _cached = (data["classifier"], data["anomaly"], data["metrics"])
            return _cached
        except Exception:
            pass
    _cached = train_models()
    return _cached

def score(amount, sender_count=0, receiver_count=0, hour=12):
    clf, anomaly, _ = load_models()
    row = np.array([[amount, sender_count, receiver_count, hour, sender_count + receiver_count]])
    probability = float(clf.predict_proba(row)[0][1])
    anomaly_flag = int(anomaly.predict(row)[0] == -1)
    # Combine classifier probability with the anomaly signal as documented indicators.
    risk = round(min(100, probability * 85 + anomaly_flag * 15), 1)
    label = "Potentially Fraudulent Transaction" if risk >= 61 else "Suspicious Transaction" if risk >= 31 else "Legitimate Transaction"
    reasons = []
    if amount > 1800: reasons.append("amount is unusually high")
    if hour < 5 and amount > 450: reasons.append("large transaction at an unusual hour")
    if sender_count > 16 and receiver_count > 12: reasons.append("high sender and receiver activity")
    if anomaly_flag: reasons.append("Isolation Forest marked the feature pattern anomalous")
    return probability, risk, label, "; ".join(dict.fromkeys(reasons)) or "No elevated risk indicators"
