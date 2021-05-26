# name=("mona arya")
# a=name.split()
# print(name)
# print(a)


# a=("mona arya")
# x=a.split()
# print(x)




# def split(a):
#     words=str(a)
#     for word in words:
#         print(word,end=" ")
# split("my name is mona")     





# def name(a):
#     i=0
#     word=str(a)
#     while i<len(a):
#         print(a[i])
#         i=i+1
# name("my name is mona arya")




# def name(a):
#     i=0
#     word=str(a)
#     while i<len(a):
#         print(a[i])
#         i=i+1
# name("my name is mona arya")


# n=[[1,2,3,4],[4,5,8,,7]]
# i=0
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         print(n[i][j])
#         j=j+1
#     i=i+1



# def name(a):
#     i=0
#     word=str(a)
#     while i<len(a):
#         j=0
#         while j<len(a[i]):
#             print(a[i][j])
#             j=j+1
#         i=i+1
# name("my name is mona arya")




a="my name is mona arya"
s=""
b=[]
for i in a:
    if i==" ":
        b.append(s)
        s=""
    else:
        s+=i
if s:
    b.append(s)
print(b)