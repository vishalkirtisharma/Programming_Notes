

def naturals(n):
    if n==1 or n==0:
        return 1
    return n + naturals(n-1)


print(naturals(300))
