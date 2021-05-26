def perfect(a):
    i=1
    sum=0
    while i<a:
        if a%i==0:
            print(i)
            sum=sum+1
        i=i+1
    if sum==0:
        print("perfect number")
    else:
        print("not a perfect number")
perfect(1)
