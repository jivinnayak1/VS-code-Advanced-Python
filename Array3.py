
num = [1,2,3,4,6,5,4,5,6,9,1,2]
print(num)
num.sort()
print(num)

n = len(num)
print(num[n-1])

N = [1,2,3,4,5,6,7,8,9,10]

N.pop(0)
N.pop(0)
N.pop(0)
N.pop(0)

print(N)

Numbers = [20,22,23,1,43,54,8,9,6,3,4]
Numbers2 = []

for item in Numbers:
    if item>5:
        Numbers2.append(item)
print(Numbers2)

Letters = ["A","B","C","D","E"]

Letters.remove("A")
Letters.remove("B")

Letters.insert(0,"F")
Letters.insert(1,"G")

Letters.reverse()
print(Letters)