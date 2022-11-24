with open("S.txt","r")  as f:
    content =f.read()

if "Python" in content:
    print (True)
else:
    print (False)