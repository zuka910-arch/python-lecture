while True:
    try:
        x = int(input("pls enter x: "))
        break
    except ValueError:
        print("გთხოვთ შემოიყავნოთ მხოლოდ ციფრი")
        continue

print(f"გილოცავთ, თვქენი რიცხვია {x}")