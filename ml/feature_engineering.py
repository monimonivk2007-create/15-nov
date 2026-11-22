"""Feature preparation shared by offline demos and documentation."""
FEATURES = ["amount", "sender_count", "receiver_count", "hour", "account_activity"]

def transaction_features(amount, sender_count, receiver_count, hour):
    return {"amount": float(amount), "sender_count": int(sender_count), "receiver_count": int(receiver_count), "hour": int(hour), "account_activity": int(sender_count) + int(receiver_count)}
