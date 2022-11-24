from tkinter import Y


mydict={
    "Fast":"In a good manner",
    "Vishal":"A coder",
    "A dict" :{"Dict": "Answer"
    },
    1:2
}

# print(type (mydict.keys()))
print(mydict.values())
print(mydict.items())
# newdict

mydict.update({"myname":"Vishal Sharma"})
print(mydict)
print(mydict.get("myname"))