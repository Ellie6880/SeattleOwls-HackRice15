from sqlalchemy import Column, Integer, String, Boolean, Boolean, Date, ForeignKey
from backend.db.base_class import Base

class Task(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index = True, nullable=False)
    dosage = Column(String, nullable=True)
    frequence = Column(String, nullable = True)
    schedule = Column(String, nullable=True)
    expiration_date = Column(Date, nullable=True)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))
