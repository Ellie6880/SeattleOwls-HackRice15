from pydantic import BaseModel
from datetime import date, time
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    home_address: str
    phone_number: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    class Config:
        from_attributes = True

class DrugBase(BaseModel):
    name: str
    description: Optional[str] = None
    side_effects: Optional[str] = None

class DrugCreate(DrugBase):
    pass

class DrugResponse(DrugBase):
    id: int
    class Config:
        from_attributes = True

class PrescriptionBase(BaseModel):
    user_id: int
    drug_id: int
    dosage: str
    time_of_day: time
    task_label: str
    start_date: date
    end_date: date

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionResponse(PrescriptionBase):
    id: int
    class Config:
        from_attributes = True
