class Programer:
    company ="Microsoft"

    def __init__(self,name,salary,language) :
        self.name= name
        self.salary =salary
        self.language =language
        print(f"Employee {self} is created")
    
    def getDetail(self):
        print(f"Hi {self.name} you are working in {self.company} and your salary is {self.salary}. \nYour work assign on {self.language}")


Vishal = Programer("Vishal",1000,"Python")
Vivek = Programer("Vivek",100,"C")
Vishesh = Programer("Vishesh",500,"JAVA")

Vishal.getDetail()
Vivek.getDetail()
Vishesh.getDetail()