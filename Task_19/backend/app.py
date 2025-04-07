from fastapi import FastAPI
from database import engine, Base
from routes import user, protected

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/auth", tags=["Authentication"])
app.include_router(protected.router, prefix="/api", tags=["Protected"])
