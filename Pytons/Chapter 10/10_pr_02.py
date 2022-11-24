class Number:
    def __init__(self,num):
        self.num = num
        print("Hi User")

    def squareRoot(self):
        print(self.num**.5)

    def squareCubet(self):
        print(self.num**3)
        


N=Number(9)

N.squareRoot()
N.squareCubet()