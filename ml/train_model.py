from backend.services.fraud_detector import train_models

if __name__ == "__main__":
    _, _, metrics = train_models()
    print("Saved synthetic demo models. Experimental holdout metrics:")
    for key, value in metrics.items(): print(f"{key}: {value}")
