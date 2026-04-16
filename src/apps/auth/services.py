from src.apps.auth.connector import user_auth_connector
from src.apps.auth.schemas import LoginRequest, RegisterRequest, TokenResponse
from src.apps.auth.utils import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from src.apps.user.schemas import UserRead


class AuthService:
    def register_user(self, register_data: RegisterRequest) -> UserRead | None:
        existing_user = user_auth_connector.get_auth_user_by_email(register_data.email)

        if existing_user is not None:
            return None

        return user_auth_connector.create_user(register_data)

    def login_user(self, login_data: LoginRequest) -> TokenResponse | None:
        auth_user = user_auth_connector.get_auth_user_by_email(login_data.email)

        if auth_user is None:
            return None

        if auth_user.password != login_data.password:
            return None

        access_token = create_access_token({"sub": auth_user.email})
        refresh_token = create_refresh_token({"sub": auth_user.email})

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            token_type="bearer",
        )

    def refresh_access_token(self, refresh_token: str) -> TokenResponse | None:
        payload = decode_token(refresh_token)

        if payload is None:
            return None

        if payload.get("type") != "refresh":
            return None

        email = payload.get("sub")
        if email is None:
            return None

        auth_user = user_auth_connector.get_auth_user_by_email(email)
        if auth_user is None:
            return None

        new_access_token = create_access_token({"sub": auth_user.email})
        new_refresh_token = create_refresh_token({"sub": auth_user.email})

        return TokenResponse(
            access_token=new_access_token,
            refresh_token=new_refresh_token,
            token_type="bearer",
        )


auth_service = AuthService()