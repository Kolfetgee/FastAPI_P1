from fastapi import APIRouter, Depends, HTTPException, Request
from src.apps.auth.dependencies import get_current_user
from src.apps.auth.schemas import (
    AuthUserData,
    LoginRequest,
    RefreshTokenRequest,
    RegisterRequest,
    TokenResponse,
)
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


@auth_router.post("/refresh", response_model=TokenResponse)
def refresh_token(refresh_data: RefreshTokenRequest):
    refreshed_tokens = auth_service.refresh_access_token(refresh_data.refresh_token)

    if refreshed_tokens is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    return refreshed_tokens


@auth_router.get("/me-dep", response_model=UserRead)
def get_me_dep(current_user: AuthUserData = Depends(get_current_user)):
    return UserRead(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
    )


@auth_router.get("/me-middleware", response_model=UserRead)
def get_me_middleware(request: Request):
    auth_user = getattr(request.state, "auth_user", None)

    if auth_user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return UserRead(
        id=auth_user.id,
        username=auth_user.username,
        email=auth_user.email,
    )

