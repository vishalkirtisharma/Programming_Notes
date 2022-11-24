

num=int(input("Please enter your No: "))

prime =True

for i in range(2, num):
    if num%i==0:
        prime=False
        break


print(prime)