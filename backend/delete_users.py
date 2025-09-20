from backend.db.session import SessionLocal
from backend.models.user import User

def delete_all_users():
    db = SessionLocal()
    db.query(User).delete()
    db.commit()
    db.close()

if __name__ == "__main__":
    delete_all_users()
    print("All users have been deleted.")