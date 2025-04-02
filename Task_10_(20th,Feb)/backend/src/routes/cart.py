from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.crud import crud
from src.schemas import schemas
from src.config import database

router = APIRouter()

@router.post("/cart/", response_model=schemas.CartItem)
def add_to_cart(cart_item: schemas.CartItemCreate, db: Session = Depends(database.get_db)):
    item = crud.add_to_cart(db, cart_item)
    if not item:
        raise HTTPException(status_code=400, detail="Not enough stock")
    return item

@router.post("/checkout/")
def checkout(db: Session = Depends(database.get_db)):
    order = crud.checkout(db)
    if not order:
        raise HTTPException(status_code=400, detail="Cart is empty or insufficient stock")
    return order

@router.get("/cart/", response_model=list[schemas.CartItem])
def get_cart(db: Session = Depends(database.get_db)):
    cart_items = crud.get_cart(db)
    return cart_items


@router.delete("/cart/{item_id}/", response_model=schemas.CartItem)
def remove_from_cart(item_id: int, db: Session = Depends(database.get_db)):
    item = crud.remove_from_cart(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found in cart")
    return item

