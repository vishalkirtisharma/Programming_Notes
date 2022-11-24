while True:
    a=input("Please enter a Number: ")
    if a=="q":
        break
    try:
        a=int(a)
        if a >6:
            print(a)
    except Exception as e:
        print(e)

print("Thanks for use this game")