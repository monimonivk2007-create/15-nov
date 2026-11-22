def risk_level(score):
    if score <= 30: return "Low"
    if score <= 60: return "Medium"
    if score <= 80: return "High"
    return "Critical"
