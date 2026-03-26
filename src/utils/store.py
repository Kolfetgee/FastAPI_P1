class Store:
    def __init__(self) -> None:
        self.users: dict[int, dict] = {}

    def __enter__(self) -> "Store":
        print("Store connection opened")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        print("Store connection closed")


store = Store()
