from src.apps.auth.connector import user_auth_connector
from src.apps.auth.schemas import RegisterRequest, LoginRequest, TokenResponse
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

        return TokenResponse(
            access_token="fake_access_token",
            refresh_token="fake_refresh_token",
            token_type="bearer"
        )





auth_service = AuthService()