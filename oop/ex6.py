class Restaurant:
    def __init__(self, restaurant_name, causine_type):
        self.restaurant_name = restaurant_name
        self.causine_type = causine_type


    def describe_restaurant(self):
        print(f"Restaurant name : {self.restaurant_name}")
        print(f"Causine type: {self.causine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, causine_type):
        super().__init__(restaurant_name, causine_type)

        self.flavors = ["Chocolate" , "Strawberry", "Mango"]

    def show_flavors(self):
        print("ice cream flavors:")

        for flavor in self.flavors:
            print(f" {flavor}")

my_icecream = IcecreamStand("sweet ice", "icecream")

my_icecream.describe_restaurant()

my_icecream.show_flavors()


class Admin()