from src.apps.user.repository import UserRepository

from src.apps.user.schemas import UserRead, UserCreate, UserUpdate
from src.apps.auth.schemas import AuthUserData


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get_user(self, user_id: int) -> UserRead | None:
        return self.repository.get_by_id(user_id)

    def get_users(self) -> list[UserRead]:
        return self.repository.get_all()

    def get_users_by_ids(self, user_ids: list[int]) -> list[UserRead]:
        return self.repository.get_by_ids(user_ids)

    def get_auth_user_by_email(self, email: str) -> AuthUserData | None:
        return self.repository.get_auth_user_by_email(email)

    def create_user(self, user_create: UserCreate) -> UserRead | None:
        existing_user = self.repository.get_by_email(user_create.email)
        if existing_user is not None:
            return None
        return self.repository.create(user_create)

    def create_many_users(self, users_in: list[UserCreate]) -> list[UserRead]:
        return self.repository.create_many(users_in)

    def update_user(self, user_id: int, user_update: UserUpdate) -> UserRead | None:
        return self.repository.update(user_id, user_update)

    def delete_user(self, user_id: int) -> UserRead | None:
        return self.repository.delete(user_id)




user_service = UserService(repository=UserRepository())