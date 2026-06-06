def get_positive_int():
    while True:
        try:
            x = int(input("შეიყვანეთ რიცხვი: "))
            if x > 0:
                return x
            else:
                print("გთხოვთ შემოიყავნოთ მხოლოდ დადებითი რიცხვი...")
            

        except ValueError:
            print("გთხოვთ შემოიყავნოთ მხოლოდ ციფრი!")


def main():
    x = get_positive_int()

    for i in range(x):
        print("#")


main()