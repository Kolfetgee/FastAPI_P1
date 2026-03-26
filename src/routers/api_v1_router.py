from fastapi import APIRouter

from src.apps.auth.routers import router as auth_router
from src.apps.user.routers import router as user_router

api_v1_router = APIRouter()
api_v1_router.include_router(user_router)
api_v1_router.include_router(auth_router)
