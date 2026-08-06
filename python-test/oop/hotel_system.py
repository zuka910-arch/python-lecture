import json

class HotelRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.is_clean = True
        self.is_occupied = False
        self.notes= []

    def check_in(self):
        self.is_occupied = True
        print(f"check in room - {self.room_number} = OK")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def check_out(self):
        self.is_clean = False
        self.is_occupied = False
        print(f"Il cliente è uscito! La camera {self.room_number} richiede lo sbarazzo!")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def add_note(self, text):
        self.notes.append({
            "informazione" : text,
            "is_done" : False,
            "reply" : ""
        })
        print("nota aggiunta!")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def show_info(self):
        print(f"camera: {self.room_number}")
        #=============================================================================================================
        if self.is_clean:
            print("Stato: Pulita")
        else:
            print("Stato: Da rifare / Sbarazzo")
        #=============================================================================================================
        if self.is_occupied:
            print("stato : Occupata")
        else:
            print("Stato : Libera")
        #===============================================================================================================
        print("Note / Ticket:")
        if not self.notes:
            print(" - Nessuna nota.")
        else:
            for i, nota in enumerate(self.notes, 1):
                if nota["is_done"]:
                    status = "✅ Fatto"
                else:
                    status = "❌ Da fare"
                print(f" {i}. [{status}] {nota['informazione']}")
                if nota["reply"]:
                    print(f"    ↳ Risposta: {nota['reply']}")
        print("---------------------------\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def complete_ticket(self, ticket_number):
        index = ticket_number - 1
        if 0 <= index < len(self.notes):
            self.notes[index]["is_done"]= True
            print("✅ Ticket completato con successo!")
        else:
            print("❌ Numero ticket non valido!")
            






#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    def to_dict(self):
        return {
            "room_number": self.room_number,
            "is_clean": self.is_clean,
            "notes": self.notes,
            "Stato": self.is_occupied
        }
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def get_num(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num  < 0 or num > 125 :
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
                room.is_occupied = room_data["Stato"]
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
    print("\n--- 🛎️ Pannello di Controllo Camere ---")
    print("1. Check-in (Aggiungi camera)")
    print("2. Check-out (Richiedi sbarazzo)")
    print("3. Dashboard & Gestione (დაფა და მართვა)")
    print("4. Esci e Salva (გასვლა და შენახვა)")
    
    choose = input("Scegli un'opzione (1/2/3/4): ")

    if choose == "1":
        num = get_num("Numero di camera per Check-in: ")
        if num in rooms_database:
            if rooms_database[num].is_occupied:
                print(f"⚠️ Attenzione! Impossibile fare il check-in. La camera {num} è già occupata!")
            elif not rooms_database[num].is_clean:
                print(f"🧹 Impossibile! La camera {num} è libera, ma deve essere pulita prima (Sbarazzo)!")

            else:
                rooms_database[num].check_in()
        else:
            rooms_database[num] = HotelRoom(num)
            rooms_database[num].check_in()

    elif choose == "2":
        num = get_num("Quale camera ha fatto il check-out? ")
        if num in rooms_database:
            rooms_database[num].check_out()
        else:
            print("Camera non trovata!")

    elif choose == "3":
        print("\n--- 📋 Camere nel Sistema ---")
        if not rooms_database:
            print("Nessuna camera registrata.")
            continue
        else:
            for num, room_obj in rooms_database.items():
                stato = "Occupata" if room_obj.is_occupied else "Libera"
                pulizia = "pulita" if room_obj.is_clean else "sbarazzo"
                tickets = len(room_obj.notes)
                print(f"🚪 Camera {num} | Stato: {stato} | Pulizia: {pulizia} | Ticket aperti: {tickets}")
        print("-----------------------------\n")

        room = get_num("Scegli il numero di camera per i dettagli (o 0 per uscire): ")
        
        if room == 0:
            continue

        if room in rooms_database:
            while True:
                rooms_database[room].show_info()
                
                print("--- ⚙️ Azioni Camera ---")
                print("1. Aggiungi Ticket (ახალი პრობლემის დამატება)")
                print("2. Segna ticket come Fatto (სტატუსის შეცვლა)")
                print("3. segna come pulita")
                print("4. Torna al menu principale (უკან დაბრუნება)")
                
                sub_choose = input("Scegli (1/2/3/4): ")
                
                if sub_choose == "1":
                    note_text = input("Inserisci il dettaglio del ticket: ")
                    rooms_database[room].add_note(note_text)
                elif sub_choose == "2":
                    t_num = get_num("Numero del ticket: ")
                    rooms_database[room].complete_ticket(t_num)
                elif sub_choose == "3":
                    rooms_database[room].is_clean = True
                    print(f"✨ La camera {room} è ora pulita!")
                    del rooms_database[room]
                    print(f"🗑️ La camera {room} è stata rimossa dal database (Pronta per check-in).")
                    break
                elif sub_choose == "4":
                    break
                else:
                    print("Scelta non valida!")
        else:
            print("Camera non trovata!")

    elif choose == "4":
        save_data(rooms_database)
        print("Arrivederci!")
        break
        
    else:
        print("Scelta non valida!")









# კოდში გასასწორებელია ჩექინის დროს და ჩექ აუთის დროს ოთახების ბაზიდან გაქრობა ან რაიმე მსგავსი, რადგან როდესაც ჩექნიზე გაშვებისას ოთახი ბაზაში ჩავარდება, შემდე ჩექაუთზე ბაზაში რცება უბრალოდ სტატუსი ეცვლება თავისუფალ ოთახს