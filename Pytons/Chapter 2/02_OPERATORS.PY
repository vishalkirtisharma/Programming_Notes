from ast import Assign, Compare, operator


a=3
b=4


#Arthmetic operators
print("the value of a+b=",a+b)
print("the value of a-b=",a-b)
print("the value of a*b=",a*b)
print("the value of a/b=",a/b)

# Assignment Operators
a=34
a+= 12
a-= 12
a*= 12
a/= 12
print(a)

# Comparision Operators
b=(14>7)
print(b)

#Logical Operators

bool1=True
bool2=False

print("The value of  bool1 and bool2 is",(bool1 and bool2))
print("The value of  bool1 or bool2 is",(bool1 or bool2))
print("The value of  not bool2 is",( not bool2))