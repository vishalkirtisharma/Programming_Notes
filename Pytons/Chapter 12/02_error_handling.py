try:
    a=int(input("Please enter a number: "))
    c=1/a
    print(c)
except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(f"Zeros {e}")

print("Thanks for this code")