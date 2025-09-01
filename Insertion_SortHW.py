A= [17,21,30,26,8]

for i in range(1, len(A)):
    value = A[i]

    j = i-1
    while j >= 0 and value <A[j]:
        A[j+1] = A[j]
        j -= 1
        A[j+1]= value


print("Sorted array")

for i in range(len(A)):
    print("%d" %A[i],end=" ")