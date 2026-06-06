def get_positive_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            if x > 0:
                return x
        except ValueError:
            print("გთხოვთ შემოივანოთ რიცხვი..")


def main():
    size = get_positive_int("რა ზომის კვადრატი გინდა? ")

    for _ in range(size):
        print("#" * size)
main()