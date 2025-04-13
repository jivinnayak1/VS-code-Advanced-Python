fruits = ["apple","mango","banana","cherry","orange"]
print(fruits[0])
print(fruits[-1])

last_element_index = len(fruits)-1
print(last_element_index)
print(fruits[last_element_index])

print(fruits[2:5])

print(fruits)
fruits.append("Guava")
fruits.append("Dragonfruit")
print(fruits)

for i in fruits:
    print(i)

print(fruits.remove("apple"))
print("fruits")