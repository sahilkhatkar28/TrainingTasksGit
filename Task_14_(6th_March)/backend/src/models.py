from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    role: str = "user"  # Default role

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    owner: str
