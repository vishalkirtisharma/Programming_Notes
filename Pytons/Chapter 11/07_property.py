class Employee:
    company ="Bharat Gas"
    salary = 5600
    salarybonus= 500
    # totalSalary = 6100  

    @property
    def totalsalary(self):
        return self.salary +self.salarybonus

    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary



e=Employee()

print(e.totalsalary)
e.totalsalary =5800 
print(e.salarybonus)
print(e.salary)