
def readFIle(fiename):
    try:
        with open(fiename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print("FIle not found")



readFIle("1.txt")
readFIle("s2.txt")
readFIle("3.txt")