import re


class Complex:
    def __init__(self,r,i) :
        self.real=r
        self.imaginery= i

    def __add__(self,c):
        return Complex(self.real +c.real, self.imaginery + c.imaginery)
    
    def __str__(self):
        return f"{self.real} + {self.imaginery}i"

    def __mul__(self,c):
        mulreal = self.real*c.real - self.imaginery* c.imaginery
        mulImg = self.real*c.imaginery + self.imaginery* c.real        
        return Complex(mulreal,mulImg )

    
c1=Complex(1,4)
c2=Complex(8,5)
 
print(c1+c2)
print(c1*c2)