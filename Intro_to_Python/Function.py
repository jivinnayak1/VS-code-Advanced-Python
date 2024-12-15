def Cube(number):
    print(number**3)

Cube(4)

def Square(number):
    print(number**2)

Square(17)

#Lambda Function

Square = lambda number : print(number**2)

Square(4)

#Lambda Function 2

Square = lambda number : print(number**2)

Numbers = [34,35,36,37,38,39,40,41,42,43,44,45,46]

Result = map(Square,Numbers)

print(list(Result))