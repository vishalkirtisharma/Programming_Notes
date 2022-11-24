import os

On = "S2.txt"
Nn = "NS2.txt"

with open(On,"r") as f:
    data = f.read()


with open(Nn,"w") as f:
    f.write(data)

os.remove(On)