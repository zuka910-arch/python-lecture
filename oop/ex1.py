class Restaurant:
    def __init__(self, restaurant_name, causine_type):
        self.restaurant_name = restaurant_name
        self.causine_type = causine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.causine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

restaurant = Restaurant("Ottocento", "Italian")
print(restaurant.restaurant_name)
print(restaurant.causine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()