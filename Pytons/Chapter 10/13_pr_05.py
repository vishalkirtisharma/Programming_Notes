
class Train:

    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat =seat
    
    def getstatus(self):
        print(f"the name of train is {self.name} and fare is {self.fare} with seat of {self.seat}")
    
    def bookticket(self,n):
        self.n=n
        if ((self.seat-self.n)>-1):
            print("your seat confirmed")
            self.seat-= self.n
        else:
            print("Seats not avaiable")
        
        


test= Train("Vishal",100,10)
Booking = True    
while Booking:
    test.getstatus()
    seat= int(input("how much seat your require: "))
    test.bookticket(seat)
    test.getstatus()
    User= input("Do you want to continue Y/N: ")
    if User.lower()=="n":
        Booking= False
        print("Thanks for using this!")