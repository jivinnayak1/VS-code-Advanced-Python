cars = ["Toyota","Bmw","Mercedes","Audi","Buggati","Citroen"]
#Calling Out Element
print(cars[0])
#Printing Range of Elements
print(cars[0:3])
#Appending New Element
cars.append("Hyundai")
print(cars)
#Removing Element
print(cars.remove("Audi"))
print(cars)
#Inserting Elememt
cars.insert(2,"Renault")
print(cars)
#Updating Element
cars[5] = "Kia"
print(cars)
#Adding Another List to Original List
cars2 = ["Chevrolet","Maybach","Mahindra","Tata","Audi","Citroen","Lamborghini"]
cars.extend(cars2)
print(cars)
#Remove Individual Index
cars.remove("Hyundai")
cars.pop(3)
print(cars)
#Finding Index of Element
index_m = cars.index("Maybach")
print(index_m)
#Clearing List
cars.clear()
print(cars)
#Number List
numbers = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,5,4,5,5,5,6]
#Finding Out How Many Times an Element Has Occured in a List
print(numbers.count(3))
#Print Elements in Reverse
numbers.reverse()
print(numbers)
#Sorting Numerals in Assending Order
numbers.sort()
print(numbers)