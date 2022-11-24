class  RailwayForm:
    formType= "RailwayForm"

    def printData(self):
        print(f"Name is {self.name} and train is {self.train}")
    



vishalApplication= RailwayForm()
vishalApplication.name ="Vishal"
vishalApplication.train= "Rajdhani Express"
vishalApplication.printData()