

def BubbleSort(arr):
    n = len(arr)
#Traverse through the array
    for i in range(n):
        #Last i elements are already in place
        for j in range(0, n-i-1):
            #Traverse the array from 0 to n-i-1
            #Swap if the element found is greater than the next element
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [54, 23, 25, 173, 332, 543,45]

BubbleSort(arr)

print ("Sorted Array:")

for i in range(len(arr)):
    print("%d" %arr[i],end=" ")