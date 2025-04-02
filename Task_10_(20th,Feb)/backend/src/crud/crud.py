from sqlalchemy.orm import Session
from src.models import all_models
from src.schemas import schemas

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = all_models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = all_models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session):
    return db.query(all_models.Product).all()

def add_to_cart(db: Session, cart_item: schemas.CartItemCreate):
    product = db.query(all_models.Product).filter(all_models.Product.id == cart_item.product_id).first()
    if not product or product.stock < cart_item.quantity:
        return None
    db_cart_item = all_models.CartItem(**cart_item.dict())
    db.add(db_cart_item)
    db.commit()
    db.refresh(db_cart_item)
    return db_cart_item

def checkout(db: Session):
    cart_items = db.query(all_models.CartItem).all()
    if not cart_items:
        return None
    for item in cart_items:
        product = db.query(all_models.Product).filter(all_models.Product.id == item.product_id).first()
        if product.stock < item.quantity:
            return None
        product.stock -= item.quantity
        db.delete(item)
    db.commit()
    return {"message": "Order placed successfully"}

def get_cart(db: Session):
    return db.query(all_models.CartItem).all()

def remove_from_cart(db: Session, item_id: int):
    item = db.query(all_models.CartItem).filter(all_models.CartItem.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return item
    return None  # If item not found
