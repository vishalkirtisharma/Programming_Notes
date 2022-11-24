def game(n):
    with open("h.txt","r") as f:
        scrore= f.read()
    if scrore=="":
        scrore=0
    if int(scrore)<n  :
        with open("h.txt","w") as f:
            f.write(str(n))

game(450)