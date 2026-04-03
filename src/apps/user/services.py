from src.apps.user.repository import UserRepository

from src.apps.user.schemas import UserRead, UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get_user(self, user_id: int) -> UserRead | None:
        return self.repository.get_by_id(user_id)

    def get_users(self) -> list[UserRead]:
        return self.repository.get_all()

    def create_user(self, user_create: UserCreate) -> UserRead:
        return self.repository.create(user_create)

    def get_users_by_ids(self, user_ids: list[int]) -> list[UserRead]:
        return self.repository.get_by_ids(user_ids)

    def update_user(self,  user_id: int, user_update: UserUpdate) -> UserRead | None:
        return self.repository.update(user_id, user_update)

    def delete_user(self, user_id: int) -> UserRead | None:
        return self.repository.delete(user_id)

    def create_many_users(self, users_in: list[UserCreate]) -> list[UserRead]:
        return self.repository.create_many(users_in)


user_service = UserService(repository=UserRepository())