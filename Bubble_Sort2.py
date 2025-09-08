def sortZeroOne(A, n):
    #Count the no fo zeros in an array
    count = 0

    for i in range(0,n):
        if (A[i] == 0) :
            count = count +1

    #Filling the A with 0 until count
    for i in range(0, count):
        A[i] = 0

    #filling remaining space with 1
    for i in range(count, n):
        A[i] = 1
    

#drive code
A= [ 0, 1,0,1,1,1]
n = len(A)

sortZeroOne(A,n)
print("Sorted Array is",end="")

for i in range(0,n):
    print(A[i], end =" ")