class Person:
    Country ="India"
    salary =100
    Location ="Delhi"

    # def Changesalary(self,sal):
    #     self.__class__.salary= sal

    @classmethod
    def Changesalary(cls,sal):
        cls.salary= sal


e=Person()
print (e.salary)
e.Changesalary(455)
print (e.salary)
print (Person.salary)
