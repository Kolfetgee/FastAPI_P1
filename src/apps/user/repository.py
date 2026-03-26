from src.utils.store import store


class UserRepository:
    def get_all(self) -> list[dict]:
        with store as db:
            return list(db.users.values())
