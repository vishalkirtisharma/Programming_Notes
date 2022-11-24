def check(num):
    if num%2==0:
        return True
    else:
        return False 

l=[1,2,3,4,5,6,7,8,9,10,11,14,16,64]

print(list(filter(check,l)))