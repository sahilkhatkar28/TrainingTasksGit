from fastapi import APIRouter, HTTPException, Depends
from bson.objectid import ObjectId  # Import ObjectId
from ..database import items_collection
from ..models import Item
from ..auth.auth_bearer import JWTBearer

router = APIRouter()

@router.post("/", dependencies=[Depends(JWTBearer())])
async def create_item(item: Item, token_data: dict = Depends(JWTBearer())):
    if token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    existing_item = items_collection.find_one({"name": item.name})
    if existing_item:
        raise HTTPException(status_code=400, detail="Item with this name already exists")

    inserted_item = items_collection.insert_one(item.dict())
    return {"msg": "Item created successfully", "id": str(inserted_item.inserted_id)}

@router.get("/{name}")
async def get_item(name: str):
    item = items_collection.find_one({"name": name})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    item["_id"] = str(item["_id"])  # Convert ObjectId to string
    return item

@router.put("/{name}", dependencies=[Depends(JWTBearer())])
async def update_item(name: str, updated_item: Item, token_data: dict = Depends(JWTBearer())):
    if token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    result = items_collection.update_one({"name": name}, {"$set": updated_item.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"msg": "Item updated successfully"}

@router.delete("/{name}", dependencies=[Depends(JWTBearer())])
async def delete_item(name: str, token_data: dict = Depends(JWTBearer())):
    if token_data["role"] != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")

    result = items_collection.delete_one({"name": name})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"msg": "Item deleted successfully"}
