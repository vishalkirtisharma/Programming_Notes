from msilib.schema import Class


class Employee:
    company= "Visa"
    Ecode=120

class FreeLancer:
    company = "Fiverr"
    level=0

    def upgradeLevel(self):
        self.level +=1


class Programmer(Employee,FreeLancer):
    name= "rohit"



p=Programmer()
print(p.level)
print(p.company)
p.upgradeLevel()
print(p.level)