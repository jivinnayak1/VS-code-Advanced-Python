def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r-l)//2

        #Check if x is present at mid
        if arr[mid] == x:
            return mid
        
        #If x is greater, ignore left half
        elif arr[mid] < x:
            l=mid+l
        
        #If x is smaller, ignore right half
        else:
            r = mid -l

        #Return -1 if element isnt found
        return -l
    #Driver Code

arr= [2,3,4,10,40]
x = 7

#Function Call
result = binarySearch(arr,0,len(arr)-1,x)

if result != -1:
    print("Element {} is present at index {}".format(x,result))
else:
    print("The element searched doesn't exist in the array")
