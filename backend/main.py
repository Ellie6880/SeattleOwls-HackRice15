from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

# Add CORS Middleware
origins = [
    "http://localhost:3000" # For Local Dev
    "https://medicinetracker.com" # For Production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users
@app.post("/register", response_model = schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code = 400, detail = "Email already registered")
    return crud.create_user(db, user)

# Drugs
@app.post("/drugs", response_model = schemas.DrugResponse)
def add_drug(drug: schemas.DrugCreate, db: Session = Depends(get_db)):
    return crud.create_drug(db, drug)

@app.get("/drugs", response_model = list[schemas.DrugResponse])
def list_drugs(db: Session = Depends(get_db)):
    return crud.get_drugs(db)

# Prescriptions
@app.post("/prescriptions", response_model = schemas.PrescriptionResponse)
def add_prescription(prescription: schemas.PrescriptionCreate, db: Session = Depends(get_db)):
    return crud.create_prescription(db, prescription)

@app.get("/prescriptions/{user_id}", response_model = list[schemas.PrescriptionResponse])
def list_prescriptions(user_id: int, db: Session = Depends(get_db)):
    return crud.get_prescriptions(db, user_id)
