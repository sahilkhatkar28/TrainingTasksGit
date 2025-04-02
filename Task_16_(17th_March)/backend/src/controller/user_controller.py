from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from src.config.database import get_db
from src.service.user_service import register_user, verify_user
from src.utils.email_utils import send_verification_email

class UserRegister(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    message: str

router = APIRouter()

@router.post("/register/", response_model=UserResponse)
def register(user: UserRegister, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    result = register_user(user.email, user.password, db)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    # Run email sending task in the background
    background_tasks.add_task(send_verification_email, user.email, result["token"])
    
    return {"message": "User registered. Verification email sent."}

@router.get("/verify-email/", response_model=UserResponse)
def verify_email(token: str, db: Session = Depends(get_db)):
    result = verify_user(token, db)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    
    return {"message": "Email verified successfully"}
