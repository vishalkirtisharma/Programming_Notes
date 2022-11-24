with open("S.txt","r")  as f:
    i=0
    content=True
    while content:
        content =f.readline()
        i +=1   
        if "Python" in content:
            print (True, i) 
      