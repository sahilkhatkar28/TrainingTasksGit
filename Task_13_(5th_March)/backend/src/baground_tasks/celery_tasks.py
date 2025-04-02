from flask import current_app

from src.config.celery_worker import celery
from flask_mail import Message
from src.config import mail  

@celery.task(name='send_registration_email')
def send_registration_email(email, username):
    msg = Message("Welcome to Our Platform",
                  sender="your_email@example.com",
                  recipients=[email])
    msg.body = f"Hello {username},\n\nWelcome to our platform. We are glad to have you!"
    
    with current_app.app_context():
        mail.send(msg)




