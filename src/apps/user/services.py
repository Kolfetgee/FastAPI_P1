from src.apps.user.repository import UserRepository
from src.apps.user.routers import user_service
from src.apps.user.schemas import UserRead, UserCreate


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository



    def get_user(self, user_id: int) -> UserRead | None:
        self.repository.get_by_id(user_id)

    def get_users(self) -> list[UserRead]:
        return  self.repository.get_all()

    def create_user(self, user_create: UserCreate) -> UserRead:
        return self.repository.create(user_create)


user_service = UserService(repository=UserRepository())