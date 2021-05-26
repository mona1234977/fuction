def c(a,l):
    i=0
    sum=0
    while i<=l:
        if(i%3==0 or i%5==0):
            sum=sum+i
            print(i)
        i+=1
    print("sum is",sum)
c(0,6)

