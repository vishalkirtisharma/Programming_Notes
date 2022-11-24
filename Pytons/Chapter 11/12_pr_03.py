class Employee:
    Salary =1000
    increment = 1.5

    @property
    def SalaryAfterIncrement(self):
        return self.Salary* self.increment

    @SalaryAfterIncrement.setter
    def  SalaryAfterIncrement(self,val):
        self.increment = (val-self.Salary)/self.Salary

e=Employee()

print(e.SalaryAfterIncrement)
e.SalaryAfterIncrement= 1200
print(e.increment)
