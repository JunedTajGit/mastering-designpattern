class Equipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Composite:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self

    @property
    def price(self):
        return sum([x.price for x in self.items])

    @price.setter
    def price(self, value):
        self.price = value


if __name__ == "__main__":
    computer = Composite("PC")
    processor = Equipment("Processor", 1000)
    hard_drive = Equipment("Hard Drive", 250)
    memory = Composite("Memory")
    rom = Equipment("Read only memory", 100)
    ram = Equipment("Randon access memory", 75)

    mem = memory.add(rom)
    mem = memory.add(ram)

    pc = computer.add(processor).add(hard_drive).add(mem)

    print(f"Total PC Price {pc.price}")
    print(f"Total Mem Price {mem.price}")
