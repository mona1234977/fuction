a=[28,17,18]
b=[30,16,9]
i=0
counta=0
countb=0
while i<len(a):
    if (a[i])<(b[i]):
        counta=counta+1
    else:
        countb=countb+1
    i=i+1
print(counta)
print(countb)
