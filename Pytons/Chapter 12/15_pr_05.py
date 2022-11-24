from turtle import st


a=int(input("Please enter a Number: "))

b = [i*a for i in range(1,11) ]
print(b)
with open("table.txt","a") as f:
    f.write(str(b))
    f.write("\n")