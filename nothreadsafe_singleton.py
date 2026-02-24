import time
from threading import Thread


class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwds):
        if self not in self._instances:
            instance = super().__call__(*args, **kwds)
            time.sleep(1)
            self._instances[self] = instance
        return self._instances[self]


class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f"{self}\n")


def create_singleton():
    singleton = NetworkDriver()
    singleton.log()
    return singleton


if __name__ == "__main__":
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)

    p1.start()
    p2.start()
