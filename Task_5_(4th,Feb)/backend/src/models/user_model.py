# BACKEND/src/models/user_model.py
from pydantic import BaseModel

class User(BaseModel):
    email: str
    name: str