class Person:
    Country ="India"

    @staticmethod
    def Breating():
        print("i am breating")


class Employee(Person):
    company="Honda"

    def getSalary(self):
        print(f"your salary is {self.salary} ")
    
    @staticmethod
    def Breating():
        print("i emplyee berthinh")
    

class Programmer(Employee):
    company="Fiverr"

    def getSalary(self):
        print(f"no Salary to programmer")

p=Person()
e=Employee()
pr=Programmer()

p.Breating()
e.Breating()