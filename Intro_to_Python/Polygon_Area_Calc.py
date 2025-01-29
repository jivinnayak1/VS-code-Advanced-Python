class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

rect = Rectangle(3, 4)
print(f"Rectangle area: {rect.area()}")

square = Square(5)
print(f"Square area: {square.area()}")
shapes = [Rectangle(3, 4), Square(5)]
