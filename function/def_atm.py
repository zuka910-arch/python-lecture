def atm():
    balance = 1000
    while True:
        try:
            amount = float(input("გთხოვთ შეიყვანოთ სასრუველი თანხა ან  ოპერაციის შესაწყვეტად დააჭირეთ Ctrl+D: "))
            if amount > balance:
                print("თანხა არ არის საკმარისი. გთხოვთ, სცადოთ ხელახლა.")
            elif amount <= 0:
                print("გთხოვთ, შეიყვანეთ დადებითი თანხა.")
            elif amount <= balance:
                balance -= amount
                print(f"თქვენ წარმატებით გაიყვანეთ {amount} ლარი. დარჩენილი ბალანსი: {balance} ლარი.")
                if balance == 0:
                    print("თქვენი ბალანსი ამოიწურა. მადლობა, რომ გამოიყენეთ ჩვენი ATM. ნახვამდის!")
                    break
                while True:
                    bamount = input("გსურთ კიდევ თანხის გამოტანა? (კი/არა): ")
                    if bamount == "yes" or bamount == "კი":
                        break
                    elif bamount == "no" or bamount == "არა":
                        print("მადლობა, რომ გამოიყენეთ ჩვენი ATM. ნახვამდის!")
                        return
                    else:
                        print("გთხოვთ, შეიყვანეთ 'კი' ან 'არა'")
                    

        except ValueError:
            print("გთხოვთ, შეიყვანეთ ვალიდური თანხა.")
        except EOFError:
            print("\n ოპერაცია შეწყდა. მადლობა, რომ გამოიყენეთ ჩვენი ATM. ნახვამდის!")
            break
       



atm()