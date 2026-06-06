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

class Privileges:
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user","can edit post"]
    def show_privileges(self):
        print("admin privileges")

        for privilege in self.privileges:
            print(f"{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, user_age, user_nationality):
        super().__init__(first_name, last_name, user_age, user_nationality)
        self.privileges= Privileges()

admin1 = Admin("zuka", "bakuradze", 25, "georgia")
admin1.describe_user()
admin1.privileges.show_privileges() 