from dataclasses import dataclass


# complex system
class ComplexSystemStore:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.cache = {}

        print(f"Reading data from file: {self.filepath}")

    def store(self, key: str, value: str):
        self.cache[key] = value

    def read(self, key: str):
        return self.cache[key]


@dataclass
class User:
    login: str


# Facade
class UserRepository:
    def __init__(self):
        self.system_prefereces = ComplexSystemStore("/data/default.db")

    def save(self, user: User):
        self.system_prefereces.store("USER_KEY", user.login)

    def find_first(self):
        return User(self.system_prefereces.read("USER_KEY"))


if __name__ == "__main__":
    user_repo = UserRepository()
    user = User("jhon")

    user_repo.save(user)

    retrived_user = user_repo.find_first()

    print(f"retrived user: {retrived_user}")
