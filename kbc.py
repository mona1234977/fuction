def kbc(question,option,solution,answer):
    print("welcome to kaun banega carorepati")
    print()
    i=0
    amount=100000
    count=0
    b=0
    a=1
    while i<len(question):
        print(question[i])
        j=0
        k=1
        while j<len(option[i]):
            print(option[i][j])
            j=j+1
        lifeline=input("do you want lifeline")
        if lifeline=="yes":
            print("5050")
            if count==0:
                print(answer[b+i])
                print(answer[b+a])
                num=int(input("enter the answer"))   
                if num==solution[i]:
                    print("your answer is right")
                    print("you won",amount)
                else:
                    print("your answer is wrong")
                    print("you loose the game")
                    break
                count=count+1
                print()
            else:
                print("you had already used the lifeline")
                e=int(input("enter the answer"))
                if e==solution[i]:
                    print("your answer is right")
                    print("you won",amount)
                else:
                    print("your answer is wrong")
                    print("you loose the game")
                print()
        else: 
            f=int(input("enter the answer"))
            if f==solution[i]:
                print("your answer is right")
                print("you won",amount)
            else:
                print("your answer is wrong")
                print("you loose the game")
                break
            print()
        amount=amount+100000
        i=i+1
        a=a+1
        b=b+1
    print("thanks for playing")
kbc((["1.how many continents are there?","2.what is the capital of india?","3.ng me kon sa course padhaya jata hai?"]),
([["1.four","2.nine","3.seven","4.eight"],["1.chandigarh","2.bhopal","3.chennai","4.delhi"],["1.software engineering","2.counseling","3.tourism","4.agriculture"]]),([3,4,1]),
(["3.seven","4.eight","3.chennai","4.delhi","1.software engineer","2.counseling"]))

