#Task 1
Square = lambda number : print(number**2)

Numbers = [1,2,3,4,5,6,7,8,9,10]

Result = map(Square,Numbers)

print(list(Result))


# Task 2

String = lambda letter : print(letter.lower())

Letters = ["A","B","C","D","E","F","G"]

PrintResult = map(String,Letters)

print(list(PrintResult))



#Task 3
Add = lambda numbers : print(numbers+5)

Number = [3,4,6,223,434,634,443,343,68,44,1,10]

PrintResults = map(Add,Number)

print(list(PrintResults))


#Task 4
def Postive_or_Negative(Number):
    
    
    
    if Number>0:
        print("Positive")
    else:
        print("Negative")

print(Postive_or_Negative(5))

def Cube(number):
    print(number**3)

Cube(4)