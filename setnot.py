def setornot (number , n):
    if number&(1 <<(n - 1)):
        print("\nset")
    else :
        print("\nnot set")
number = int(input("enter the number"))
n = int(input("enter the bit number "))
setornot(number , n)