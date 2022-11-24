from glob import glob


a=54 #global
def fun1():
    global a
    print(a )
    a=8
    print(a)


fun1()
print(a)