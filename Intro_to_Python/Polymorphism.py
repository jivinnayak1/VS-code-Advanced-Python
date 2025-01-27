# class Rectangle:
#     def Area(self,Height,Width):
#         return Height*Width
    
# class Square:
#     def Area(self,Height,Width):
#         return Height*Width
    
# Box = Rectangle()
# print(Box.Area(8,10))

# Box2 = Square()
# print(Box2.Area(8,8))

class Dog:
    def Sound(self,sound):
        print(sound)
        

class Cat:
    def Sound(self,sound):
        print(sound)
        

Cat_Sound = Cat()
print(Cat_Sound.Sound("Meow"))

Dog_Sound = Dog()
print(Dog_Sound.Sound("Woof"))