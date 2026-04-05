from fastapi import APIRouter


from src.apps.user.routers import user_router

api_v1_router = APIRouter()
api_v1_router.include_router(user_router)

