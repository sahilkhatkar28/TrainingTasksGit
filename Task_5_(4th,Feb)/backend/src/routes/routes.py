# BACKEND/src/routes/api.py
from fastapi import APIRouter
from src.controller import auth_controller

router = APIRouter()
router.include_router(auth_controller.router, tags=["auth"])