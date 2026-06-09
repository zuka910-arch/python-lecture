class HotelRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_clean = True

    def check_in(self):
        print(f"check in room - {self.room_number} = OK")

    def check_out(self):
        self.is_clean = False
        print(f"Il cliente è uscito! La camera {self.room_number} richiede lo sbarazzo!")

#HOTEL menu
def get_num(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num  <= 0 or num > 125 :
                print("Per favore, inserisci un numero di camera valido (1-125)!") 
                continue

            else:
             return num
        except ValueError:

            print("Inserisci solo numeri validi!")
            continue

rooms_database = {}
while True:
    print("--- 🛎️ Pannello di Controllo Camere --- \n" \
        "1. Check-in (Aggiungi camera) \n" \
        "2. Check-out (Richiedi sbarazzo) \n" \
        "3. Esci dal programma \n")
    choose = input("Scegli un'opzione (1/2/3): ")
    if choose == "1":
            num = get_num("Numero di camera: ")
            rooms_database[num] = HotelRoom(num)
            rooms_database[num].check_in()
    elif choose == "2":
            num = get_num("Quale camera ha fatto il check-out?   ")
            if num in rooms_database:
                rooms_database[num].check_out()
            else:
                print("Camera non trovata!")
    elif choose == "3":
        print("arrivederci")
        break
    else:
        print("choose error")

    

