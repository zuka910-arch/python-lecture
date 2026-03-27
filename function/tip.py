def calculate_tip():
    amount = int(input("შეიყვანეთ თანხა: ").strip())
    tip = amount * 0.10
    floated_tip = float(tip)

    print(f"თქვენი თიფსი არის {floated_tip:.2f} ევრო")



calculate_tip()