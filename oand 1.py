def num(n):
    zero = 0
    one = 0

    while  n: 
        if n&1 == 1 :
            one +=1
        else :
            zero+=1
        n>>=1
    print("total numbers of 0 are" , zero)
    print("total numbers of 1 are" , one)
num(3)