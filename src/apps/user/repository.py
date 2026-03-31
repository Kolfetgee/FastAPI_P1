from src.apps.user.schemas import UserRead, UserCreate, UserUpdate
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

    def update(self, user_id: int, user_update: UserUpdate) -> UserRead | None:
        with get_store() as store:
            user_data = store.users.get(user_id)
            if user_data is None:
                return None

            for field_name, field_value in user_update.model_dump().items():
                if field_value is not None:
                    user_data[field_name] = field_value

            return UserRead(
                id=user_data["id"],
                username=user_data["username"],
                email=user_data["email"]
            )

    def delete(self,user_id: int)-> UserRead | None:
        with get_store() as store:
            deleted_user_data = store.users.pop(user_id, None)
            if deleted_user_data is None:
                return None
            return UserRead(
                id=deleted_user_data["id"],
                username=deleted_user_data["username"],
                email=deleted_user_data["email"]
            )
    def get_by_ids(self, user_ids: list[int]) -> list[UserRead]:
        with get_store() as store:
            found_users = []

            for user_id in user_ids:
                user_data = store.users.get(user_id)
                if user_data is not None:
                    found_users.append(UserRead(
                        id=user_data["id"],
                        username=user_data["username"],
                        email=user_data["email"]
                    )
                    )

            return found_users
