import json

class HotelRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_clean = True
        self.notes= []

    def check_in(self):
        print(f"check in room - {self.room_number} = OK")

    def check_out(self):
        self.is_clean = False
        print(f"Il cliente è uscito! La camera {self.room_number} richiede lo sbarazzo!")
    def add_note(self, text):
        self.notes.append(text)
        print("nota aggiunta!")
    def show_info(self):
        print(f"camera: {self.room_number}")
        if self.is_clean:
            print("Stato: Pulita")
        else:
            print("Stato: Da rifare / Sbarazzo")
        print(f"info : {self.notes}")

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "is_clean": self.is_clean,
            "notes": self.notes
        }
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def save_data(database):
    data_to_save = {}
    for num , room_obj in database.items():
        data_to_save[num] = room_obj.to_dict()
    with open("hotel_data.json", "w") as file:
        json.dump(data_to_save, file, indent=4)

#====================================================================================================================================
def load_data():
    loaded_db = {}
    try:
        with open("hotel_data.json", "r") as file:
            data_loaded = json.load(file)
            for num, room_data in data_loaded.items():
                real_num = int(num)
                room = HotelRoom(room_data["room_number"])
                room.is_clean = room_data["is_clean"]
                room.notes = room_data["notes"]
                loaded_db[real_num] = room
        print("Dati caricati con successo!\n")
        return loaded_db
    except FileNotFoundError:
        print("Nessun dato salvato trovato. Inizio con database vuoto.\n")
        return {}
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#HOTEL menu

rooms_database  = load_data()
while True:
    print("--- 🛎️ Pannello di Controllo Camere --- \n" \
            "1. Check-in (Aggiungi camera) \n" \
            "2. Check-out (Richiedi sbarazzo) \n" \
            "3. Aggiungi nota (კომენტარის დამატება) \n" \
            "4. Mostra info camera (ინფორმაციის ნახვა) \n" \
            "5. Esci e Salva (გასვლა და შენახვა) \n")
    choose = input("Scegli un'opzione (1/2/3/4/5): ")
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
        room =get_num("quale camera?")
        if room in rooms_database:
            note = input("comment")
            rooms_database[room].add_note(note)
        else:
            print("camera non trovata!")
    elif choose == "4":
        room = get_num("Numero di camera: ")
        if room in rooms_database:
            rooms_database[room].show_info()
        else:
            print("camera non trovata!")

    elif choose == "5":
        save_data(rooms_database)
        print("arrivederci")
        break
    else:
        print("choose error")