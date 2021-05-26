def d(l):
    if(l==2 or l==3):
        print(l,"is a prime number")
    elif(l%2==0 or l%3==0):
        print(l,"is not a prime number")
    else:
        print(l,"is a prime number")
    return(l)
d(7)
