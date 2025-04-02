from fastapi import APIRouter, HTTPException, Depends
from pymongo.errors import DuplicateKeyError
from ..database import users_collection
from ..models import User
from pydantic import BaseModel
from ..auth.auth_handler import hash_password, verify_password, create_access_token
from ..auth.auth_bearer import JWTBearer

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
async def register_user(user: User):
    user_exists = users_collection.find_one({"email": user.email})
    if user_exists:
        raise HTTPException(status_code=400, detail="User already exists")

    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return {"msg": "User registered successfully"}

@router.post("/login")
async def login(request: LoginRequest):
    user = users_collection.find_one({"email": request.email})
    if not user or not verify_password(request.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"username": user["username"], "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me", dependencies=[Depends(JWTBearer())])
async def read_users_me(token_data: dict = Depends(JWTBearer())):
    return {"username": token_data["username"], "role": token_data["role"]}