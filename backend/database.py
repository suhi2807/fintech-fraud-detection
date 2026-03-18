from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["fintech_db"]

transactions = db["transactions"]

fraud_logs = db["fraud_logs"]