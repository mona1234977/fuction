def a(b):
    i=0
    c=b[0]
    k=[]
    while i<len(b):
        if b[i]<c:
            c=b[i]
        i=i+1
    print(c)
k=[4,5,6,7,67,8,5,23,2]
a(k)




# def split(a):
#     words=str(a)
#     for word in words:
#         print(word,end="  ")
# split("mona")



# def split(a):
#     i=0
#     words=str(a)
#     while i<len(a):
#         if a in words:
#             print(words,end=" ")
#         i=i+1
#     print(words)
# split(a)
# a="mona arya"
# a.split()
# print(a)