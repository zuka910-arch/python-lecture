ages = {
    "shako": 26,
    "natia": 25,
    "zuka": 25,
}


input_name = input("Enter a name: ").lower().strip()
if input_name in ages:
    print(f"{input_name} is {ages[input_name]} years old.")
else:
    print(f"{input_name} is not in the dictionary.")
    input_age = int(input("Enter the age for this name: "))
    ages[input_name] = input_age
    print(f"{input_name} has been added to the dictionary with age {input_age}.")
    print(ages)