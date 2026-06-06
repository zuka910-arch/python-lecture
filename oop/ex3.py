class User:
    def __init__(self, first_name, last_name, user_age, user_nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_nationality = user_nationality
    
    def describe_user(self):
        print(f"user firstname: {self.first_name}")
        print(f"user lastname: {self.last_name}")
        print(f"user age: {self.user_age}")
        print(f"user nationality: {self.user_nationality}")


    def great_user(self):
        print(f"hello,{self.first_name}")


user0 = User("zuka", "bakuradze", 25, "georgia")
user1 = User("nata", "jimsheleishvili", 24, "georgia")
user2 = User("alessandro", "coppoteli", 43, "itly")

user0.great_user()
user1.great_user()
user2.great_user()
    