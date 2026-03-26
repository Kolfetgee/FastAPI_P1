from src.apps.user.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get_all_users(self) -> list[dict]:
        return self.repository.get_all()
