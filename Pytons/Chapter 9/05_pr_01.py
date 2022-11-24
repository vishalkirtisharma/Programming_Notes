f= open("poem.txt","r")
a=f.read()

print("twinkle" in a.lower())
f.close()