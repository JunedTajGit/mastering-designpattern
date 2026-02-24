class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwds):
        if self not in self._instances:
            instance = super().__call__(*args, **kwds)
            self._instances[self] = instance

        return self._instances[self]


class NetworkDrivers(metaclass=Singleton):
    def log(self):
        print(f"{self}\n")


def create_singleton():
    singleton = NetworkDrivers()
    singleton.log()
    return singleton


if __name__ == "__main__":
    # single thread
    s1 = create_singleton()
    s2 = create_singleton()
