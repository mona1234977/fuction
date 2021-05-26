# list=[]
# i=5
# while i>0:
# # for i in list:
#     a=input("enter the task")
#     list.append(a)
#     i=i-1
# print(list)
# b=input("enter the task")
# if b in a:
#     list.remove(a)
#     # list.append(b)
#     i=i+1
# print(a)


# list=["study","breakfast","lunch","snacks"]
# a=input("enter the task")
# list.append(a)
# print(list)
# b=input("enter the task would you like to remove from the list")list=["study","breakfast","lunch","snacks"]
# a=input("enter the task")
# list.append(a)
# print(list)
# b=input("enter the task would you like to remove from the list")
# list.remove(a)
# print(a)


n=int(input("enter the number"))
i=0
a=[]
while i<n:
    list=input("enter the task")
    a.append(list)
    i=i+1
print(a)
c=input("enter the task")
if n in a:
    a.remove(n)
    print(a)
else:
    print("it is not in list")



