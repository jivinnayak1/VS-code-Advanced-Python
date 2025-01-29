class Shape:
    def __init__(self, name):
        self._name = name

    def area(self):
        pass
    
    
    def display(self):
        print(f"{self._name} Area: {self.area()}")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._name = "Square"

shapes = [Rectangle(4, 5), Square(3)]

for shape in shapes:
    shape.display()

