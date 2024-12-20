MyList1 = ["Jivin","Subhadeep","Vivaan","Jhonny"]
MyList2 = [1,2,3,4,5,6,7]
MyList3 = [1.2,3.4,5.3,34.5]
MyList4 = [True, False, True, True]

#Printing Singular Data Typed
firstname = MyList1[0]
print(firstname)

print("")

#Updating Data
MyList1[0] = "Jivin Nayak"
print(MyList1)

print("")

#Deleting DataTypes
del MyList1[1]
print(MyList1)

print("")

#Deleting DataTypes through Element Names
MyList1.remove("Vivaan")
print(MyList1)

print("")

#Viewing Last Element
print(MyList1.pop())

#Adding Element
MyList1.append("Arjun")
print(MyList1)