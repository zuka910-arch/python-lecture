rooms = {
    "coffe": 2,
    "water": 1.5,
    "cocacola": 3,
    "beer": 2.5,
    "cocktail": 8}

  
guest_drinks = input("რა გსურთ? (coffe, water, cocacola, beer, cocktail)").strip().lower()
guest_cart = []
while True:
    if guest_drinks in rooms:
        print(f"{guest_drinks} საფასური არის {rooms[guest_drinks]} ლარი.")
        guest_cart += [guest_drinks]
        guest_drinks = input("გსურთ კიდევ რამე? (coffe, water, cocacola, beer, cocktail)").strip().lower()
        if guest_drinks == "no":
            print(f"თქვენი შეკვეთა: {guest_cart}")
            break
    else:
        print("სამწუხაროდ, ჩვენთან ასეთი სასმელი არ გვაქვს.")
        guest_drinks = input("გსურთ კიდევ რამე? (coffe, water, cocacola, beer, cocktail)").strip().lower()
        if guest_drinks == "no":
            print(f"თქვენი შეკვეთა: {guest_cart}")
            break

total_price = 0
for drink in guest_cart:
    total_price += rooms[drink]
print(f"თქვენი შეკვეთის ჯამური ფასი არის {total_price} ლარი.")