from pymongo import MongoClient
from .config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client.fastapi_db  # Database name
users_collection = db.users
items_collection = db.items
