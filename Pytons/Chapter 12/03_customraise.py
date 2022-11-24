def increment(num):
    try:
        return int(num) +1
    except:
        raise ValueError("error found")


a=increment("a")

print(a)