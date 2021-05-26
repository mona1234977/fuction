def d(l):
    i=0
    a=[]
    while i<len(l):
        if l[i] not in a:
            a.append(l[i])
        i+=1
    print(a)
d(l=[1,2,3,3,3,4,4,7,0,0,9,8,8,7,6,5])

