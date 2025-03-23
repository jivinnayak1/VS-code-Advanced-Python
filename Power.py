# print(6)
# print(bin(6))
# print(8)
# print(bin(8))
# print(6&8)
# print(bin(6&8))

# a = 5
# b = 2

# print(bin(a))
# print(bin(b))
# print(bin(a<<b))

# for i in range(1,11):
#     print(bin(i))

def Even_Odd(number):
    if number & 1 == 1:
        return "Odd"
    else:
        return "Even"
    
print(Even_Odd(5))