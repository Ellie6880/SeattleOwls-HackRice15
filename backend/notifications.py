import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
from backend.models import User, Prescription, Drug
from backend.database import SessionLocal
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

def send_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_sms(to_phone, body):
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to_phone
        )
        print(f"SMS sent to {to_phone}")
    except Exception as e:
        print(f"Failed to send SMS: {e}")

def send_reminder(prescription: Prescription):
    db = SessionLocal()
    try:
        # Get user info
        user = db.query(User).filter(User.user_id == prescription.user_id).first()
        if not user:
            return

        # Get drug info
        drug = db.query(Drug).filter(Drug.drug_id == prescription.drug_id).first()
        if not drug:
            return

        body = f"Reminder: {prescription.task_label}\n" \
               f"Dosage: {prescription.dosage}\n" \
               f"Drug: {drug.drug_name}\n" \
               f"Time: {prescription.time_of_day}\n" \
               f"Please take your medication on time!"

        if user.email:
            send_email(user.email, "Medication Reminder", body)
        if user.phone_number:
            send_sms(user.phone_number, body)
    finally:
        db.close()
