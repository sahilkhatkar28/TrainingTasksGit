from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = None
    user_id:int

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
