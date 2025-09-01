def merge_sort(A):
    if len(A)>1:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]

        #Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        #Two Iterators for traversing the two halves

        i = 0
        j = 0

        #Iterator for the main array
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                #Take value from the left half has been used
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            #Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1

A = [59,80,38,17,90,31,56,55,21]
print("Unsorted Array: {}".format(A))
merge_sort(A)
print("Sorted Array: {}".format(A))