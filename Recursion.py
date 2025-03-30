# def Number(n):
#     if n ==1:
#         print(n)
#         return
#     print(n)
#     Number(n-1)

# Number(100)

# import math

# print(math.factorial(2))

def Factorial(n):
    if n==1 or n==0:
        return 1
    result = n*Factorial(n-1)
    return result

print(Factorial(4))