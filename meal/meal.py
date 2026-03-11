def main():
    time = input("What time is it? ").strip()
    hours = convert(time)
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")
def convert(time):
    time = time.lower()

    if "a.m." in time:
        is_pm = False
        time = time.replace("a.m.", " ").strip()
    elif "p.m." in time:
        is_pm = True
        time = time.replace("p.m.", " ").strip()
    else:
        is_pm = False


    
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if is_pm and hours != 12:
        hours = hours + 12
    elif not is_pm and hours == 12:
        hours = 0
    return hours + minutes / 60


if __name__ == "__main__":
    main()