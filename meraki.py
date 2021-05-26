numbers=[3,5,7,34,2,89,2,5]
print(max(numbers))


def r(s):
    d={"UPPER_CASE":0,"LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print("original string:",s)
    print("number of uppercase letters:",d["UPPER_CASE"])
    print("number of lowercase letters:",d["LOWER_CASE"])
r("the quick brown fox")
