letter='''Dear <#name>,
you are selected on <#date>'''
name = input("Plase enter a name")
date = input("Plase enter a Date")
letter= letter.replace("<#name>",name)
letter= letter.replace("<#date>",date)
print(letter)