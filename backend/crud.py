from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

# User CRUD
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(
        username = user.username,
        email = user.email,
        first_name = user.first_name,
        last_name = user.last_name,
        home_address = user.home_address,
        phone_number = user.phone_number,
        password = hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Drug CRUD
def create_drug(db: Session, drug: schemas.DrugCreate):
    db_drug = models.Drug(**drug.dict())
    db.add(db_drug)
    db.commit()
    db.refresh(db_drug)
    return db_drug

def get_drugs(db: Session):
    return db.query(models.Drug).all()

# Prescription CRUD
def create_prescription(db: Session, prescription: schemas.PrescriptionCreate):
    db_prescription = models.Prescription(**prescription.dict())
    db.add(db_prescription)
    db.commit()
    db.refresh(db_prescription)
    return db_prescription

def get_prescriptions(db: Session, user_id: int):
    return db.query(models.Prescription).filter(models.Prescription.user_id == user_id).all()
