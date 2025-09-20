# backend/reset_database.py
from backend.database import SessionLocal, engine, Base
from backend import models

def reset_database():
    # Drop all tables
    Base.metadata.drop_all(bind = engine)
    # Recreate them
    Base.metadata.create_all(bind = engine)

    print("✅ Database has been reset.")

if __name__ == "__main__":
    reset_database()
