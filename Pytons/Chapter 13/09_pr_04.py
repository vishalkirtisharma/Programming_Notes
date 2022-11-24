from logging import Filter


l=[5,10,12,13,150,20]

b= list(filter(lambda a:a%5==0,l))
print(b) 