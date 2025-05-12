import math

# Array = [1,2,3]
# Sub1 = [1]
# Sub2 = [2]
# Sub3 = [3]
# Sub4 = [1,2]
# Sub5 = [2,3]
# Sub6 = [1,2,3]

# Max = 6

Array = [3,4,5,6]

S1 = [3] #=3
S2 = [4] #=4
S3 = [5] #=5
S4 = [6] #=6
S5 = [3,4] #=7
S6 = [4,5] #=9
S7 = [5,6] #=11
S8 = [3,4,5] #=12
S9 = [4,5,6] #=15
S10 = [3,4,5,6] #=18

Max = max(323,34,324,34,453,25,37)

print(Max)

def kadan(arr):
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max (current_sum,max_sum)
    return max_sum
print(kadan([-1,-2,2,3]))

# max = current = -2

# max = current = -2

# num = -1

# current = max(-1,-2+-1) = max(-1,-3) = -1

# max = max(-1,-2) = -1

# num = 2

# cuerrent = max(2,-1+2) = max(2,1) = 2

# max = max(2,-1) = 2

# mum = 3

# current = max(3,2+3) = max(3,5) = 5

# max = max(5,2) = 5

# max = 5