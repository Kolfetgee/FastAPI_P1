from fastapi import APIRouter, HTTPException
from src.apps.auth.schemas import RegisterRequest, TokenResponse, LoginRequest
from src.apps.auth.services import auth_service

from src.apps.user.schemas import UserRead

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.post("/register", response_model=UserRead)
def register_user(register_data: RegisterRequest):
    created_user = auth_service.register_user(register_data)

    if created_user is None:
        raise HTTPException(status_code=409, detail="User with this email already exists")

    return created_user

@auth_router.post("/login", response_model=TokenResponse)
def login_user(login_data: LoginRequest):
    user_login = auth_service.login_user(login_data)

    if user_login is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return user_login