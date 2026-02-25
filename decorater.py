from abc import ABC, abstractmethod


# 3rd party library on which we don't any control.
# this is how a abstract method is created in python
class CoffeeMachine(ABC):
    @abstractmethod
    def make_small_coffee(self):
        pass

    @abstractmethod
    def make_large_coffee(self):
        pass


class BasicCoffeeMachine(CoffeeMachine):
    def make_small_coffee(self):
        print("Basic coffee machine: making small coffee")

    def make_large_coffee(self):
        print("Basic coffee machine: Making large Coffee")


class EnchancedCoffeeMachine(CoffeeMachine):
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine

    # using existing functionality from parent object
    def make_small_coffee(self):
        self.basic_machine.make_small_coffee()

    def make_large_coffee(self):
        print("Enhanced coffee machine: Making milk coffee")

    # using existing functionality + Add new functionality
    def make_milk_coffee(self):
        print("Enchanced coffee machine: Making milk coffee")
        self.basic_machine.make_small_coffee()
        print("Enchanced coffee machine: adding milk")


if __name__ == "__main__":
    basic_machine = BasicCoffeeMachine()
    EnchancedCoffeeMachine = EnchancedCoffeeMachine(basic_machine=basic_machine)

    EnchancedCoffeeMachine.make_small_coffee()
    print()
    EnchancedCoffeeMachine.make_large_coffee()
    print()
    EnchancedCoffeeMachine.make_milk_coffee()
