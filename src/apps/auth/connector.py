from src.apps.auth.schemas import AuthUserData, RegisterRequest
from src.apps.user.schemas import UserCreate, UserRead
from src.apps.user.services import user_service


class UserAuthConnector:
    def get_auth_user_by_email(self, email: str) -> AuthUserData | None:
        return user_service.get_auth_user_by_email(email)

    def create_user(self, register_data: RegisterRequest) -> UserRead | None:
        user_create = UserCreate(
            username=register_data.username,
            email=register_data.email,
            password=register_data.password,
        )
        return user_service.create_user(user_create)


user_auth_connector = UserAuthConnector()