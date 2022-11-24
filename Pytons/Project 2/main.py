import random

randnum = random.randint(1,100)
print(randnum)
i=0
userguess= None

while not randnum== userguess:
    userguess= int(input("Please enter a number Between 1-100"))
    i +=1

    if randnum > userguess:
        print("Please increase your guess")
    elif randnum < userguess:
        print("Please reduce your guess")
else:
    with open("score.txt","r") as f:
        sc= f.read()
        if int(sc) >i:
            with open("score.txt","w") as f:
                f.write(str(i))
    print(f"you have done in {i} times") 