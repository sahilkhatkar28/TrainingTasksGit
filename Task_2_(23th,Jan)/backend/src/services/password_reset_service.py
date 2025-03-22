from flask_mail import Message
from flask import url_for
from src.config.database import get_db
from itsdangerous import URLSafeTimedSerializer
from src.config.config import Config, mail, bcrypt

def generate_token(email):
        seralizer = URLSafeTimedSerializer(Config.SECRET_KEY)
        return seralizer.dumps(email,salt='password-reset-salt')


def verify_token(token,expiration=3600):
        seralizer = URLSafeTimedSerializer(Config.SECRET_KEY)
        try:
            email = seralizer.loads(token,salt='password-reset-salt',max_age=expiration)
            return email
        except Exception:
            return None


def request_password_reset(email):
    """
    Handle a user's request to reset their password.
    Sends an email with a secure token link.
    """
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    if not user:
        return {"error": "User with this email does not exist"}, 404

    token = generate_token(email)
    reset_url = url_for('password_reset_bp.reset_password_controller', token=token, _external=True)
    send_reset_email(email, reset_url)
    return {"message": "Password reset email sent"}, 200

def send_reset_email(email, reset_url):
    """
    Send the password reset email to the user.
    """
    try:
        msg = Message(
            subject="Password Reset Request",
            recipients=[email],
            body=f"Click the following link to reset your password: {reset_url}"
        )
        mail.send(msg)
    except Exception as e:
        print(f"Error sending reset email: {e}")

def reset_password(token, new_password):
    """
    Verify token and reset the user's password.
    """
    email = verify_token(token)
    if not email:
        return {"error": "Invalid or expired token"}, 400

    if not new_password or len(new_password) < 6:
        return {"error": "Password must be at least 6 characters long"}, 400

    hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
    db = get_db()
    db.execute("UPDATE users SET password = ? WHERE email = ?", (hashed_password, email))
    db.commit()

    return {"message": "Password has been reset successfully"}, 200
