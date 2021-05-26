def p(w):
    i=1
    c=1
    while i<w:
        if w%i==0:
            c+=1
        i+=1
    if w==1:
        print(w,"it is integer")
    elif c==2:
        print(w,"is a prime number")
    else:
        print(w,"is not a prime number")
p(11)