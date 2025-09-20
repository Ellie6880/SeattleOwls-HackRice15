import pandas as pd
from backend.database import SessionLocal
from backend.crud import create_user
from backend.models import Drug
from backend.crud import create_prescription

def load_users(file_path):
    df = pd.read_csv(file_path)
    db = SessionLocal()
    for _, row in df.iterrows():
        user_data = row.to_dict()
        if "password" not in user_data:
            user_data["password"] = "defaultpassword"
        create_user(db, user_data)
    db.close()

def load_drugs(file_path):
    df = pd.read_csv(file_path)
    db = SessionLocal()
    for _, row in df.iterrows():
        drug = Drug(**row.to_dict())
        db.add(drug)
    db.commit()
    db.close()

def load_prescriptions(file_path):
    df = pd.read_csv(file_path)
    db = SessionLocal()
    for _, row in df.iterrows():
        create_prescription(db, row.to_dict())
    db.close()
