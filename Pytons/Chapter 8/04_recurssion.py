
# Function Area
# def factorial_iter(n):
#     a=1
#     for i in range(n):
#         a= a*(i+1)
#     return a



# factorial(4)
# 4* factorial(3)
# 4 * [3 * factorial(2)]
# 4 * [3 *[2 * factorial(1)]]
# 4 * [3 *[2 * 1]] factorial return
def  factorial_recurssion(n):
    if n==1 or n == 0:
        return 1
    return n * factorial_recurssion(n-1)


# Code Area
f=5
# print(factorial_iter(f))

print(factorial_recurssion(f))