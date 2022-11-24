class Employee:
    company ="Google"
    
    def showDetails(self):
        print("This is an employee")

class Programer(Employee):
    Language="python"
    def getLanguage(self):
        print(f"the language is {self.Language}")
    def showDetails(self):
        print("This is an Programer")


e=Employee()
p=Programer()

e.showDetails()
p.getLanguage()
p.showDetails()
print(p.company)