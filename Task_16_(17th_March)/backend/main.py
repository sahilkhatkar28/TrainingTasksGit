from fastapi import FastAPI
from src.config.database import engine, Base
from src.routes.user_routes import router as user_router

app = FastAPI(title="FastAPI Email Verification")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user_router, prefix="/api")
