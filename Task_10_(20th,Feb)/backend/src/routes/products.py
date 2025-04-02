from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.crud import crud
from src.schemas import schemas
from src.config import database

router = APIRouter()

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    return crud.create_product(db, product)

@router.get("/products/", response_model=list[schemas.Product])
def get_products(db: Session = Depends(database.get_db)):
    return crud.get_products(db)
