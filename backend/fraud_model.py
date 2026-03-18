# fraud_model.py

def detect_fraud(amount):

    if amount > 20000000:
        return 1
    elif amount > 10000009:
        return 0.5
    return 0


def explain_fraud(amount):
    try:
        if amount > 20000000:
            return "High-value transaction detected. Risk is high."
        elif amount > 10000000:
            return "Moderate transaction. Needs verification."
        return "Low-risk transaction."

    except:
        return "AI service unavailable"