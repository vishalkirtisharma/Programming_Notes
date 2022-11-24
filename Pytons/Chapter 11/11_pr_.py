class Animal:
    Animaltype="Mamal"

class Pet(Animal):
    color = "white"

class Dog(Pet):
    def __init__(self):
        print("Bhaw Bhaww")


d=Dog()
print(d.color)
print(d.Animaltype)