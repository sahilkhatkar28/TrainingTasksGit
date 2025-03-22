from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.models import models
from src.services import schemas, crud
from src.config.database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
