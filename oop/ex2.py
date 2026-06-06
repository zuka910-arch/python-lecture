class Restaurant:
    def __init__(self, restaurant_name, causine_type):
        self.restaurant_name = restaurant_name
        self.causine_type = causine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.causine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")

restaurant0 = Restaurant("Ottocento", "Italian")
restaurant1 = Restaurant("alibaba", "shawarma city XD")
restaurant2 = Restaurant("machakhela", "GEORGIAN")
print(restaurant0.restaurant_name)
print(restaurant0.causine_type)
restaurant0.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

restaurant0.open_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()