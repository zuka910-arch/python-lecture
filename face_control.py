#blacklist = ["Dato", "Nika", "Sandro"]
#queue = ["Zuka", "Dato", "Anna", "Nika", "Luka", "Sandro", "Mariami"]

#entered_club = []  # აქ ვყრით მათ, ვინც შევიდა
#kicked_out = []    # აქ ვყრით მათ, ვინც დაცვამ გააგდო

#for guest in queue:
#    if guest in blacklist:
#        print(f"დაცვამ გააგდო{guest}")
#        kicked_out.append(guest)
#    else:
#        print(f"კეთილი იყოს თქვენი მობრზანება {guest}")
#        entered_club.append(guest)

#print(f"დაცვამ გაყარა ეს ხალხი - {kicked_out}")
#print(f"კლუბში არიან ეს ხალხი-- {entered_club}")


                               #აასაკზეც შემოწმება:

#queue = [
#    {"name": "Zuka", "age": 22},
#    {"name": "Dato", "age": 16},
#    {"name": "Anna", "age": 25},
#    {"name": "Nika", "age": 17},
#    {"name": "Mariami", "age": 20}
#]

#entered_club = []
#kicked_out = []

#for guest in queue:
#    if guest["age"] > 18:
#        print(f"კეთილი იყოს თქვენი მობრძანება  {guest}")
#        entered_club.append(guest)
#    else:
#        print("სამწუხაროდ კლუბში დაიშვებიან მხოლოდ სრულწლოვნები")
#        kicked_out.append(guest)
#print("კლუბში არიან:  ")
#for guest in entered_club:
#    print(f"[*] {guest}")
#print("კლუბიდან გავუშვით: ")
#for guest in kicked_out:
#    print(f"[*] {guest}")

                                #ცოცხალი ფეისკონტროლი

entered_club = []
kicked_out = []

while True:
    try:
        guest = input("pls  enter your name:")
        guest_age = int(input("pls enter your age: "))

        if guest_age >= 18:
            print("agred")
            entered_club.append(guest)
        else:
            print("სამწუხაროდ კლუბში დაიშვებიან მხოლოდ სრულწლოვნები")
            kicked_out.append(guest)

            









    except ValueError:
        print("გთოხვთ ასაკი შეიყვანოთ მხოლოდ რიცხვებით!")
        continue
    except EOFError:
        print("")
        print(f"კლუბში არიან: {entered_club}")
        print(f"სამწუხაროდ კლუბში არ დაიშვნენ: {kicked_out}")
        break
           
