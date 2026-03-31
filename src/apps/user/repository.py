from src.apps.user.schemas import UserRead, UserCreate
from src.utils.store import get_store


class UserRepository:
    def get_by_id(self, user_id: int) -> UserRead | None:
        with get_store() as store:
            user_data = store.users.get(user_id)

            if user_data is None:
                return None

            return UserRead(**user_data)
    def get_all(self) -> list[UserRead]:
        with get_store() as store:
            users = []

            for user_data in store.users.values():
                users.append(UserRead(**user_data))

            return users

    def create(self, user_in: UserCreate) -> UserRead:
        with get_store() as store:
            new_id = max(store.users.keys(), default=0) + 1
            new_user = {
                "id": new_id,
                "username": user_in.username,
                "email": user_in.email,
                "password": user_in.password
            }
            store.users[new_id] = new_user
            return UserRead(
                id=new_user["id"],
                username=new_user["username"],
                email=new_user["email"]
            )