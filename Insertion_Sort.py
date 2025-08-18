#Program for Insertion Sort
A= [140,4,43,84,32]
#traverse through the array
for i in range(1, len(A)):
    value = A[i]

    #Move elements of A[0..i-1], that are greater than value, to one position ahead of their current position
    j = i-1
    while j >= 0 and value <A[j]:
        A[j+1] = A[j]
        j -= 1
        A[j+1]= value

#Driver Code

print("Sorted array")

for i in range(len(A)):
    print("%d" %A[i],end=" ")