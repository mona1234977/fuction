def n(a,b):
    i=0
    k=[]
    while i<=b:
        c=(i,"=",i*i)
        i=i+1
        k.append(c)
    print("{",k,"}")
n(0,5)