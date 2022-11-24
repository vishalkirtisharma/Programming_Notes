from ssl import RAND_status


def star(n):
    for i in range(n):
        print("*" * (n-i))
        


print(star(4))