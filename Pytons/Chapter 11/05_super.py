class Person:
    Country ="India"

    def __init__(self):
        print("Intial person")

    # @staticmethod
    def Breating(self):
        print("i am breating")


class Employee(Person):
    company="Honda"

    def __init__(self):
        super().__init__() 
        print("Intial Employee")

    def getSalary(self):
        print(f"your salary is {self.salary} ")
    
    # @staticmethod
    def Breating(self):
        super().Breating()
        print("i emplyee berthinh")
    

class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print(f"no Salary to programmer")
    
    # @staticmethod
    def Breating(self):
        super().Breating()
        print("i programer berthinh")

# p=Person()
e=Employee()
pr=Programmer()

# p.Breating()
# e.Breating()
pr.Breating()