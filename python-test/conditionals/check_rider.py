def check_rider(height, age):
    if height < 140 or age < 12:
        return "ბოდიში, შენ ვერ ახვალ ატრაქციონზე"
    elif  age <= 18:
        return "შეგიძლიათ ასვლა! ბილეთის ფასი 10 ლარი"
    else:
        return "შეგიძლია ასვლა, ბილეთის ფასია 20 ლარი"
    



def main():
    cm = int(input("თქვენი სიმაღლე?"))
    age = int(input("ასაკი?"))
    result = check_rider(cm , age)
    print(result)

main()