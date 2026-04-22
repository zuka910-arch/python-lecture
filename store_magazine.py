store ={ 
    "Laptop":{"price": 1500, "stock": 3},
    "Phone": {"price": 800, "stock": 5},
    "Headphones": {"price": 150, "stock": 0}
}

cart = {}
total = 0
while True:
    try:
        item =input("item: ").title()
        if item in store:
            if store[item]["stock"] > 0:
                store[item]["stock"] -= 1
                print(f"maragshi darcha: {store[item]["stock"]} -cali")
                if item in cart:
                    cart[item] += 1
                    total +=  store[item]["price"]
                else:
                    cart[item] = 1
                    total +=  store[item]["price"]
                
                print(f"Tqven sheidzinet nivti, gadasaxdeli Tanxa: {store[item]["price"]} lari")
                print(f"tqveni kalata:{cart}")
                print(total)
            elif store[item]["stock"] == 0:
                print("samcuxarod maragi amocurulia")
        else:
            print("samcuxarod es nivti gakidvashi ar gvakvs")
    except EOFError:
        print("naxvamdis, karg dghes gisruvebt")
        break