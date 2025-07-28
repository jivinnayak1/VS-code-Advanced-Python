# Method

def isPairSum(A, N, X):
	# represents first pointer
	i = 0
	# represents second pointer
	j = N - 1

	while i < j:
		# If we find a pair
		if A[i] + A[j] == X:
			return [A[i], A[j]]
		# If sum of elements at current pointers is less, move towards higher values
		elif A[i] + A[j] < X:
			i += 1
		# If sum of elements at current pointers is more, move towards lower values
		else:
			j -= 1
	return 0

# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 15

print("Pair with the sum equal to {} is {}".format(val, isPairSum(arr, len(arr), val)))