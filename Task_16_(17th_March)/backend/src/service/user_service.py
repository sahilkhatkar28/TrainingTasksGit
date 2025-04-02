from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import BackgroundTasks
from src.models.user import User
from src.security.auth import create_verification_token, decode_verification_token
from src.utils.email_utils import send_verification_email

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def register_user(email: str, password: str, db: Session):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return {"error": "Email already registered"}
    
    hashed_password = pwd_context.hash(password)
    new_user = User(email=email, password=hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_verification_token(email)

    return {"message": "User registered. Verification email sent.", "token": token}

def verify_user(token: str, db: Session):
    email = decode_verification_token(token)
    if not email:
        return {"error": "Invalid or expired token"}

    user = db.query(User).filter(User.email == email).first()
    if not user:
        return {"error": "User not found"}

    user.is_verified = True
    db.commit()
    return {"message": "Email verified successfully"}
