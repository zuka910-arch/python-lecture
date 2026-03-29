def main():
    x = get_int()
    print(f"x is {x}")

 # ვარიანტი 1
#def get_int():
#    while True:
#        try:
#            x = int(input("x: "))
#        except ValueError:
#            print("x is not a number")
#        else:
#            break
#    return x

            #ეს მოკლე ვერსია და იგივეს აკეთებს აბრუნებს იქს და წყვეტს ციკლს,
            #  იწერება break-ის ნაცვლად
            #return x  

#main() 


#ვარიანტი 2
def get_int():
    while True:
        try:
            return int(input("x: "))
        except ValueError:
            pass #ამ შემთხვევაში მომხარებელი ვერ ხედავს რომ რაღაც არასწორია, მაგრამ 
                 #პროგრამა არ იშლება და ისევ ითხოვს რიცხვს, სანამ არ მიაწვდის
                 # სწორ რიცხვს.


            #print("x is not a number") ამ შემთხვევაში ეუბნება მომხარებელს რომ
                                        #მხოლოდ რიცხვი უნდა შეიყვანოს და არაფერი
                                        #  გარდა რიცხვისა
                                        
        



main()