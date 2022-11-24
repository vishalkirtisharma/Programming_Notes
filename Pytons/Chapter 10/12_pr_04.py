class Number:
    def __init__(self,num):
        self.num = num
        print("Hi User")

    def squareRoot(self):
        print(self.num**.5)

    def squareCubet(self):
        print(self.num**3)

    @staticmethod
    def greet():
        print("Thanks for the using this.")
        


N=Number(9)

N.squareRoot()
N.squareCubet()
N.greet()