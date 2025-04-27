fruits = ["Apple","Banana","Orange","Mango","Pineapple"]
#Call out element
print(fruits[3])
#Slice
print(fruits[0:4])
#Add Fruits
fruits.append("Guava")
print(fruits)
#Remove Fruits
print(fruits.remove("Apple"))
print(fruits)
#Insert
fruits.insert(2,"Guava")
print(fruits)
#Update Element
fruits[0] = "Guava"
print(fruits)
#Adding Another List to Original List
Cars = ["Toyota","BMW","Mercedes","Audi","Lamborghini","Hyundai"]
fruits.extend(Cars)
print(fruits)
#Remove Individual Index
Cars.remove("BMW")
Cars.pop(1)
print(Cars)
#Finding Index of Element
index_m = Cars.index("Toyota")
print(index_m)
#Clearing List
Cars.clear()
print(Cars)
#Number List
numbers = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5]
#How many times an element has occured in a List
print(numbers.count(1))
#Print Elements of List in Reverse
numbers.reverse()
print(numbers)
#Sorting Numerals In Assending Order
numbers.sort()
print(numbers)