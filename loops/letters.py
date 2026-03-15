def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "zuka"]
    for name in names:
        print(write_letter(name, "princess peach"))
def write_letter(receiver, sender):
    return f"""
   +-----------------------------------------------------+
   Dear {receiver},

   you are cordially invited to a ball at
   Peach's Castle this evning, 7:00 PM.

    Sincerely,
    {sender}
   +-----------------------------------------------------+

"""


 




main()