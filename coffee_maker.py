class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"water:{self.resources['water']}ml")
        print(f"milk:{self.resources['milk']}ml")
        print(f"coffee:{self.resources['coffee']}gm")


    def is_resources_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not sufficient ingredients")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"here is your {order.name} enjoy.")
