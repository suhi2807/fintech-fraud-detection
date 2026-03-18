from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import transactions, fraud_logs
from fraud_model import detect_fraud, explain_fraud

import uuid
from datetime import datetime

# Initialize app
app = FastAPI()

# ✅ CORS (IMPORTANT for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Home route
@app.get("/")
def home():
    return {"message": "Fintech Fraud Detection API Running"}

# ✅ Buy API with AI explanation
@app.get("/buy")
def buy_product(user_id: str, product_id: str, amount: int):

    try:
        transaction_id = str(uuid.uuid4())

        # 🔍 Fraud detection
        fraud = detect_fraud(amount)

        # 🤖 AI explanation
        explanation = explain_fraud(amount)

        # 📦 Save transaction
        transaction = {
            "transaction_id": transaction_id,
            "user_id": user_id,
            "product_id": product_id,
            "amount": amount,
            "fraud": fraud,
            "ai_explanation": explanation,
            "timestamp": str(datetime.now())
        }

        transactions.insert_one(transaction)

        # 🚨 Fraud case
        if fraud == 1:
            fraud_logs.insert_one({
                "transaction_id": transaction_id,
                "reason": "High amount transaction",
                "status": "blocked"
            })

            return {
                "status": "fraud",
                "message": "❌ Fraud detected. Transaction blocked",
                "ai": explanation
            }

        # ⚠ Suspicious case
        elif fraud == 0.5:
            return {
                "status": "suspicious",
                "message": "⚠ Suspicious transaction. Verification needed",
                "ai": explanation
            }

        # ✅ Success case
        return {
            "status": "success",
            "message": "✅ Payment successful",
            "ai": explanation
        }

    except Exception as e:
        return {
            "status": "error",
            "message": "Something went wrong",
            "error": str(e)
        }