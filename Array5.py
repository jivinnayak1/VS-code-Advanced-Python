# N = [0,0,0,0,0,3,2,4,0,1,1,1,1,1,3,3,5,4,2,2,1,2,1,5,3,2,1,5,3,1]

# for i in N:
#     if i == 0:
#         N.remove(i)
#         N.append(i)

# print(N)

Number = [1,2,3,4,5,6,7,8,9,10]

Even = []
Odd = []

for i in Number:
    if i%2 ==0:
        Even.append(i)
    else:
        Odd.append(i)

print(Even)
print(Odd)