
def maximums(n1,n2,n3):
    if n1 > n2:
        a=n1
    else:
        a= n2
    
    if a>n3:
        return a
    else:
        return n3
    
    
print(maximums(1,2,3))