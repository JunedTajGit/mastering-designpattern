from dataclasses import dataclass


# 3rd party code or Adaptee
@dataclass
class DisplayDataType:
    index: float
    data: str


class DisplayData:
    def __init__(self, display_data: DisplayDataType):
        self.display_data = display_data

    def show_data(self):
        print(
            f"3rd party functionality: {self.display_data.index} - {self.display_data.data}"
        )


# our code or test data
@dataclass
class DatabaseType:
    position: int
    amount: int


class StoreDatabaseData:
    def __init__(self, database_data: DatabaseType):
        self.database_data = database_data

    def store_data(self, data):
        print(
            f"Database data stored: {self.database_data.position} -  {self.database_data.amount}"
        )


class DisplayDataAdapter(StoreDatabaseData, DisplayData):
    def __init__(self, data):
        self.data = data

    def store_data(self):
        print("Call out code but use 3rd party code")
        for item in self.data:
            ddt = DisplayDataType(float(item.position), str(item.amount))
            self.display_data = ddt
            self.show_data()


def generate_data():
    data = list()

    data.append(DatabaseType(3, 4))
    data.append(DatabaseType(5, 6))
    data.append(DatabaseType(7, 8))

    return data


if __name__ == "__main__":
    adapter = DisplayDataAdapter(generate_data())
    adapter.store_data()
