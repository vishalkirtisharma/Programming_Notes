from winsound import SND_ALIAS


class Employee:
    company ="Google"

    def __init__(self,name,address):
        self.name= name
        self.address=address
        print(f"Employee is created in {self.name} and {self.address}")

    def getDetail(self):
        print(f"The name of employee is {self.name}")

    def getSalary(self,sign):
        print(f"My salary is {self.salary} in {self.company} \n \t {sign}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Vishal =Employee("Vishal","Haridwar")
Vishal.getDetail()
