class animal:
    eyes = 2
    ears = 2
    canWalk = True


dog = animal()

print(dog.eyes)


class OIS:
    def __init__(self,grade,students):
        self.grade = grade
        self.students = students

G7 = OIS("7", 1000)
G8 = OIS("8",3000)

print(G8.students)
print(G7.students)
print(G8.grade)
print(G7.grade)

class Sound:

    def DogSound(self):
        print("Bark")
    
    def CatSound(self):
        print("Meow")

noise = Sound()
print(noise.CatSound())
    
class animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def makeSound(self):
        print(f"{self.name} makes {self.sound} Sounds")

dog = animal("Dog","Bark")
cat = animal("Cat","Meow")

print(cat.makeSound())
print(dog.makeSound())