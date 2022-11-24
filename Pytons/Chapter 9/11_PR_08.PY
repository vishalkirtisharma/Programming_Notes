F1 = "h.txt"
F2= "S.txt"

with open(F1,"r") as a1:
    B1= a1.read()


with open(F2,"r") as a2:
    B2= a2.read()


if B2== B1:
    print(True)
else:
    print(False)