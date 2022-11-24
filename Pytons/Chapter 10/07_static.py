from winsound import SND_ALIAS


class Employee:
    company ="Google"
    def getSalary(self,sign):
        print(f"My salary is {self.salary} in {self.company} \n \t {sign}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Vishal =Employee()
Vishal.salary= 500
# Vishal.greet()
Vishal.getSalary("Thanks")