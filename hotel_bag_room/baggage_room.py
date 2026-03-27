baggage_room = {
    "101": "2",
    "102": "4",
    "103": "5",

}



while True:
    bag = input("რომელი ოთახის ბარგი მიგაქვთ?  ").strip()
    if bag == "exit":
        break
    elif bag in baggage_room:
        print(f"თქვენ ოთახისთვის დატოვებულია {baggage_room[bag]}")
    else:
        print("თქვენი ბარგი ვერ მოიძებნა")