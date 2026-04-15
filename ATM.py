balance = 1000
while True:
    
    print("1.balance")
    print("2.თანხის გატანა")
    print("3.თანხის შეტანა")
    print("4.სესიის დასრულება")
    choice = input("აირჩიეთ მოქმედება(1,2,3,4): ")

    if choice == "1":
        print(balance)
    elif choice == "2":
        cash = int(input("რა თანხის გატანა გსურთ?"))
        if cash <= balance:
          balance -= cash
          print(f"თანხის გატანა: {cash}")
          print(f"დარჩენილი თანხა: {balance}")
        else:
           print("თანხა არასაკმარისია")     
    elif choice == "3" :
       cash1 = int(input("რამდენის შეტანა გსურთ?"))
       balance += cash1
       print(balance)
    elif choice == "4":
       print("სესია დასრულებულია, გთხოვთ აიღოთ თქვენი ბარათი")
       break
    