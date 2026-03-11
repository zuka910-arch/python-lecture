def main():
    x = int(input("x= "))
    if is_even(x):
        print("x is even.")
    else:
        print("x is odd.")

def is_even(n):
   return  True if n % 2 == 0 else False
     #იგივეა შემოკლებით
   #return n % 2 == 0 
   
   #იგივეა მაგრამ უფრო გრძელი ფორმით
   #if n % 2 == 0:
    #   return True
   #else:
    #    return False


main()






