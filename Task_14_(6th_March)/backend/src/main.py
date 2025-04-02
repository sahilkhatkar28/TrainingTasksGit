from fastapi import FastAPI
from .routes import users, items

app = FastAPI(title="FastAPI MongoDB JWT API")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI MongoDB API"}
