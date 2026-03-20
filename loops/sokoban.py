def main():
    history = []

    while True:
        action = input("Action: ")                                  



        if action == "undo":
            undone = history.pop(calculate_index(history))
        else:
            history.append(action)

            
        print(history)

# def calculate_index(lst):
#     sum = 0
#     for i in  range(len(lst)):
#         sum += i
#     return round(sum / len(lst))

#print(calculate_index(["up", "down", "left", "right"]))


main()