database = {}
while True:
    try:
        name = input("Name: ").strip().lower()
        if name.isalpha() == False:
            print("Please enter a valid name.")
            continue
        if name == "stop":
            break
        if name == "delete":
            del_name = input("Enter the name to delete: ").strip().lower()
            if del_name in database:
                database.pop(del_name)
                print(f"{del_name} has been deleted from the database.")            
                print(database)
                continue
            else:
                print(f"{del_name} is not in the database.")
                continue
                
        age = int(input("Age: "))
        city = input("City: ").strip().lower()
        if city.isalpha() == False:
            print("Please enter a valid city.")
            continue
        gender = input("gender: ").strip().lower()
        if gender not in ["male", "female"]:
            print("Please enter a valid gender.")
            continue
        database[name] = [age, city, gender]
    except ValueError:
        print("Please enter a valid age.")
        continue
for name, (age, city, gender) in database.items():
    print(f"{name} is {gender} and is {age} years old and lives in {city}.")