from fastapi import FastAPI
from src.routes.routes import router
from starlette.middleware.sessions import SessionMiddleware
from src.config.config import SECRET_KEY  # Import your SECRET_KEY

app = FastAPI()
app.include_router(router)

# Add SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)