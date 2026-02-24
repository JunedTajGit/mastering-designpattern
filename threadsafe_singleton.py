import time

# import Lock to lock a thread and prevent runtime to create mulitple instances.
from threading import Thread, Lock


class Singleton(type):
    _instances = {}
    _lock = Lock()

    def __call__(self, *args, **kwds):
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args, **kwds)
                time.sleep(1)
                self._instances[self] = instance

        return self._instances[self]


class NetworkDriver(metaclass=Singleton):
    def log(self):
        print(f"{self}\n")


def create_singleton():
    Singleton = NetworkDriver()
    Singleton.log()
    return Singleton


if __name__ == "__main__":
    p1 = Thread(target=create_singleton)
    p2 = Thread(target=create_singleton)

    p1.start()
    p2.start()
