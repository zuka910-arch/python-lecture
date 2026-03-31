def check_in():
    while True:
        name = input("შეიყვანეთ თქვენი სახელი:  ").strip().lower()
        if not name.isalpha():
            print("გთხოვთ, შეიყვანეთ სწორი სახელი.")
        elif name.isalpha():
            break
    
     
    while True:

        try:
            room_number = int(input("შეიყვანეთ თქვენი ოთახის ნომერი: ").strip())

            if room_number <= 0:
                print("გთხოვთ, შეიყვანეთ სწორი ოთახის ნომერი.")
            else:
                break
        except ValueError:
            print("გთხოვთ, შეიყვანეთ ნომერი ციფრებით.")    
    

    print(f"მოგესალმებით, {name}! თქვენი ოთახის ნომერია {room_number}.")




check_in()
