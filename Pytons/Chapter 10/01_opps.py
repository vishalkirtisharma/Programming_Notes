# a=12
# b=34


# print(a+b)

class Number:
    def sum(self):
        return self.a +self.b



num = Number()
num.a = 10
num.b=25
c=num.sum()
print(c)