answer = input("do you agree? (yes/no) ").strip().lower()
  #ეს უკეთესია რადგან მხოლოდ yes და y-ით დაწყებული პასუხები იქნება მიღებული,
#if answer == "yes" or answer == "y":
#   print("You agreed.")
 

     #მაგრამ ეს არ არის გამართული, რადგან რაც y-ით იწყება ყველაფერი იმუშავებს და არა მარტო yes-ით და y-ით. ამიტომ უნდა გამოვიყენოთ startswith მეთოდი, რომელიც შეამოწმებს იწყება თუ არა y-ით.:
if answer.startswith("y"):
    print("You agreed.")
else:
    print("You did not agree.")