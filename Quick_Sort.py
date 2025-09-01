def partition(A, low, high):
	pivot = A[high]
	i = low - 1
	for j in range(low, high):
		if A[j] <= pivot:

			i = i + 1
	
			(A[i], A[j]) = (A[j], A[i])

	(A[i + 1], A[high]) = (A[high], A[i + 1])


	return i + 1


def quickSort(A, low, high):
	if low < high:

		pi = partition(A, low, high)

		quickSort(A, low, pi - 1)

		quickSort(A, pi + 1, high)
		
A = [34,54,123,22,45,23,12,64,92,16]
print("Unsorted Array: ")
print(A)

n = len(A)-1

quickSort(A,0,n)
print("Sorted Array: ")
print(A)