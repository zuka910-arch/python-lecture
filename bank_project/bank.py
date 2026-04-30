import json
import os
from datetime import datetime
from getpass import getpass


DB_FILE = "db.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"users": {}}
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=2)

def register():
    username = input("choose a username: ").strip()
    if not username:
        print("username cannot be empty")
        return
    db = load_db()
    if username in db["users"]:
        print("username is already taken.")
        return
    password = getpass("choose a password: ")
    if not password:
        print("password cannot be empty")
        return
    db["users"][username] = {
        "password": password,
        "balance": 0.0,
        "transactions": [],
    }
    save_db(db)
    print(f"Account created for '{username}'")

def login():
    username = input("username: ").strip()
    password = getpass("password: ")
    db = load_db()
    user = db["users"].get(username)
    if user is None or user["password"] != password:
        print("Invalid username or password")
        return None
    print(f"Welcome back, {username}")
    return username

def show_balance(username):
    db = load_db()
    print(f"current balance {db["users"][username]["balance"]:.2f}")

def read_amount(prompt):
    raw = input(prompt).strip()
    try:
        amount = float(raw)
    except ValueError:
        print("that's not valid number.")
        return None
    if amount <= 0:
        print("Amount must be greater than zero")
        return None
    return round(amount, 2)

def add_transaction(user, entry):
    user["transactions"].append({
        **entry,
         "at": datetime.now().isoformat(timespec="seconds"),
    })

def deposit(username):
    amount = read_amount("Amount to deposit: $")
    if amount is None:
        return
    db = load_db()
    user = db["users"][username]
    user["balance"] += amount
    add_transaction(
        user,
        {
            "type": "deposit",
            "amount": amount,
        },
        )
    save_db(db)
    print(f"Deposited ${amount:.2f}. new balance: ${user["balance"]:.2f}")
    

def user_menu(username):
    while True:
        print(f"\n--- logged in as {username} ---")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Logout")
        choice = input("choose an option: ").strip()
        if choice == "1":
            show_balance(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            print("logged out.")
            return
        else:
            print("invalid choice.")
def main():
    while True:
        print("\n=== simple bank ===")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register()
            
        elif choice == "2":
            user = login()
            if user:
               user_menu(user)
        elif choice == "3":
            print("Goodbye")
            return
        else:
            print("invalid choice.")

if __name__ == "__main__":
    main()
    