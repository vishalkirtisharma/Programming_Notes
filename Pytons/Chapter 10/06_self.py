from winsound import SND_ALIAS


class Employee:
    company ="Google"
    def getSalary(self):
        print(f"My salary is {self.salary} in {self.company}")

Vishal =Employee()
Vishal.salary= 500
Vishal.getSalary()