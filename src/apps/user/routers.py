from fastapi import APIRouter

from src.apps.user.repository import UserRepository
from src.apps.user.services import UserService

router = APIRouter(prefix="/users", tags=["Users"])

user_repository = UserRepository()
user_service = UserService(user_repository)


@router.get("/")
def get_all_users():
    return user_service.get_all_users()
