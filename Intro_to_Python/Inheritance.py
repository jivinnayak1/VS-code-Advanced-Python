class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender


class Employee(Person):
    def __init__(self,name,age,gender,id,salary):
        super().__init__(name,age,gender)
        self.id = id
        self.salary = salary


p1 = Person("Jivin",25,"Male",)
emp = Employee(p1.name,p1.age,p1.gender,1234,"$2500000")
print(emp.salary)
print(emp.name)
