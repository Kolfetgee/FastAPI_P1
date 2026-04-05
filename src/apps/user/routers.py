
from fastapi import APIRouter


from src.apps.user.schemas import UserCreate, UserRead, UserUpdate
from src.apps.user.services import user_service

user_router = APIRouter(prefix="/users", tags=["Users"])

@user_router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    return user_service.get_user(user_id)

@user_router.get("/", response_model=list[UserRead])
def get_users():
    return user_service.get_users()

@user_router.post("/", response_model=UserRead)
def create_user(user_create: UserCreate):
    return user_service.create_user(user_create)

@user_router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate):
    return user_service.update_user(user_id, user_update)

@user_router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: int):
    return user_service.delete_user(user_id)