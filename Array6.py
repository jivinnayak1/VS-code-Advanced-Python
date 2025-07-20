# fruits = ["Banana","Apple","Mango","Dragon Fruit","Orange"]

# # print(fruits[4])

# # print(fruits[1:3])
# # fruits.append("Guava")

# # fruits.remove("Apple")

# # fruits.insert(2,"Kiwi")

# # fruits[4] = "Pineaple"
# # Veggies = ["Cucumber","Eggplant","Lettuce","Carrot"]

# # fruits.extend(Veggies)

# # print(fruits)

# # index_m = fruits.index("Dragon Fruit")
# # print(index_m)

# fruits.clear()
# print(fruits)

# Numbers = [1,2,3,2,2,1,3,2,2,2,1,2,3,4,2,2,2,3,2,5,6,4,5,6,5,7,6,7,5,8,9,8,7,8,9,0,8,6,5,5,3,3,2]

# print(Numbers.count(5))

# Numbers.reverse()
# print(Numbers)

# Numbers.sort()
# print(Numbers)

#1. Create a list of 5 numbers. Use a loop to find the sum of all numbers in the list and print the result.

# Number = [1,4,3,5,7]

# total = 0

# for number in Number:
#     total+= number

# print(total)

#You have a list of numbers. Write a program to find and print only the even numbers.

NUMBERS = [1,4,3,5,7,2,4,6,4,8]

for number in NUMBERS:
    if number%2==0:
        print(number)