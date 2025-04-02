import aiosmtplib
from email.message import EmailMessage
from src.config.config import SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD

async def send_verification_email(email: str, token: str):
    msg = EmailMessage()
    verification_link = f"http://127.0.0.1:8000/api/user/verify-email?token={token}"
    msg.set_content(f"Click the link to verify your email: {verification_link}")

    msg["Subject"] = "Verify Your Email"
    msg["From"] = SMTP_USERNAME
    msg["To"] = email

    await aiosmtplib.send(
        msg, hostname=SMTP_SERVER, port=SMTP_PORT,
        start_tls=True, username=SMTP_USERNAME, password=SMTP_PASSWORD
    )
