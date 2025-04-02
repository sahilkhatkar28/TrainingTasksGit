from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.crud import crud
from src.schemas import schemas
from src.config import database

router = APIRouter()

@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(database.get_db)):
    return crud.create_category(db, category)
