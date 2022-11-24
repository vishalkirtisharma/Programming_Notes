import random


def game(C,b):
    if C== b:
        return None
    elif C == "S" and b=="G":
        return True
    elif C == "S" and b=="W":
        return False
    elif C == "W" and b=="S":
        return True
    elif C == "W" and b=="G":
        return False 
    elif C == "G" and b=="W":
        return True
    elif C == "G" and b=="S":
        return False
    
  

a = random.randint(1,3)
if a== 1:
    C="S"
elif a== 2:
    C="W"
else:
    C="G"

b= input(" Player 1 turn: Snake(S), Water(W), Gun(G)? ")

a=game(C,b)


if a== None:
    print(f"Game tie both select {C}")
elif a== True:
    print( f"You Win Com Select {C} and you Select {b}")
elif a== False:
    print( f"You Loose Com Select {C} and you Select {b}")

