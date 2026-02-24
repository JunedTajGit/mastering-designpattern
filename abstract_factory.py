from abc import ABC, abstractmethod


class FoodType:
    french = 1
    american = 2


# this is how abstract class is define in python.
class Restaurant(ABC):
    @abstractmethod
    def make_food(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass


class FrenchRestaurant(Restaurant):
    def make_food(self):
        print("Cordon bleu")

    def make_drink(self):
        print("Merlot")


class AmericanRestaurant(Restaurant):
    def make_food(self):
        print("Hamburger")

    def make_drink(self):
        print("Coca cola")


class ResturantFactory:
    # @staticmethod
    def suggest_restaurant(r_type: FoodType):
        if r_type == FoodType.french:
            return FrenchRestaurant()
        else:
            return AmericanRestaurant()


def dine_at(restaurant: Restaurant):
    print("For a dinner we are having")
    restaurant.make_food()
    restaurant.make_drink()


if __name__ == "__main__":
    suggestion1 = ResturantFactory.suggest_restaurant(FoodType.french)
    suggestion2 = ResturantFactory.suggest_restaurant(FoodType.american)

    dine_at(suggestion1)
    dine_at(suggestion2)
