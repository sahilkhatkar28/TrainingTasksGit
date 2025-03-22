from fastapi import FastAPI
from  src.models import models
from src.config.database import engine
from src.routes import users, tasks




models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Task Management API"}

