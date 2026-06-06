menu ={
    "წყალი":1,
    "ყავა":3,
    "ლუდი": 7,
    "აპეროლი":8,
    "კამპარი":9
}

total = 0

while True:
    order = input("რას ინებებთ? დასასრულებლად დაწერეთ 'end' ")
    
    if order == "end":
        print(total)
        break 

    if order in menu:
       total += menu[order]
    else:
        print("სამწუხაროდ კონკრეტული პროდუქტი ამ ეტაპზე არ გვაქვს")  

      
