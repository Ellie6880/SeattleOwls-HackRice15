from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from backend.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, unique = True, index = True)
    email = Column(String, unique = True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    home_address = Column(String)
    phone_number = Column(String)

    prescriptions = relationship("Prescription", back_populates = "user")

class Drug(Base):
    __tablename__ = "drugs"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, index = True)
    description = Column(String)
    side_effects = Column(String)

    prescriptions = relationship("Prescription", back_populates = "drug")

class Prescription(Base):
    __tablename__ = "prescriptions"
    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    drug_id = Column(Integer, ForeignKey("drugs.id"))
    dosage = Column(String)
    time_of_day = Column(Time)
    task_label = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)

    user = relationship("User", back_populates = "prescriptions")
    drug = relationship("Drug", back_populates = "prescriptions")
