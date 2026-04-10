
from fastapi import APIRouter, HTTPException, Query


from src.apps.user.schemas import UserCreate, UserRead, UserUpdate
from src.apps.user.services import user_service

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/by-ids", response_model=list[UserRead])
def get_users_by_ids(user_ids: list[int] = Query(...)):
    return user_service.get_users_by_ids(user_ids)


@user_router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    found_user = user_service.get_user(user_id)
    if found_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return found_user


@user_router.get("/", response_model=list[UserRead])
def get_users():
    return user_service.get_users()


@user_router.post("/", response_model=UserRead)
def create_user(user_create: UserCreate):
    created_user = user_service.create_user(user_create)
    if created_user is None:
        raise HTTPException(status_code=409, detail="User with this email already exists")
    return created_user


@user_router.post("/many", response_model=list[UserRead])
def create_many_users(users_in: list[UserCreate]):
    return user_service.create_many_users(users_in)


@user_router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user_update: UserUpdate):
    found_user = user_service.update_user(user_id, user_update)
    if found_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return found_user


@user_router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: int):
    found_user = user_service.delete_user(user_id)
    if found_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return found_user




