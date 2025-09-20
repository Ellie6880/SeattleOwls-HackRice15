from apscheduler.schedulers.background import BackgroundScheduler
from backend.database import SessionLocal
from backend.models import Prescription
from backend.notifications import send_reminder
from datetime import datetime, timedelta

scheduler = BackgroundScheduler()

def check_prescriptions():
    db = SessionLocal()
    now = datetime.now()
    prescriptions = db.query(Prescription).all()
    for p in prescriptions:
        if p.start_date <= now.date() <= p.end_date:
            presc_time = datetime.combine(now.date(), p.time_of_day)
            reminder_time = presc_time - timedelta(minutes=15)
            if reminder_time <= now < presc_time:
                send_reminder(p)
    db.close()

def start_scheduler():
    scheduler.add_job(check_prescriptions, 'interval', minutes=1)
    scheduler.start()
