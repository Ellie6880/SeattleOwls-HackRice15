from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class TaskBase(BaseModel):
    title: str
    drug_name: Optional[str] = None
    completed: Optional[bool] = False
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    schedule: Optional[str] = None
    expiration_date: Optional[date] = None

class TaskCreate(TaskBase):
    title: str = Field(..., example = "Take allergy pills")
    drug_name: str = Field(..., example = "Cetirizine")
    dosage: str = Field(..., example = "10mg")
    frequency: str = Field(..., example = "Once daily")
    expiration_date: date = Field(..., example = "2025-12-31")

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int
    title: str
    drug_name: str
    dosage: str
    frequency: str
    expiration_date: date

    class Config:
        orm_mode = True
