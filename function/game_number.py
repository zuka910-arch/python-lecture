def game_number():
    secret_number = 69
    tries = 10
    used_tries = 0
    while True:
        try:
            gues = int(input("Guess the number: "))
            tries -= 1
            used_tries += 1

            if gues == secret_number:
                print(f"ყოჩაღ შენ გამოიცანი ციფრი {secret_number}, {used_tries} ცდაში!")
                break
            elif gues < secret_number:
                print("ჩემი ციფრი უფრო მეტია")
            else:
                print("ჩემი ციფრი უფრო ნაკლებია")
            if tries == 0:
                print(f"სამწუხაროდ, თქვენ წააგეთ თამაში. ჩემი ციფრი იყო {secret_number}")
                break
            print(f"ცდა: {tries}")
        except ValueError:
            print("გთხოვთ შეიყვანოთ მხოლოდ ციფრები")
        
                







game_number()