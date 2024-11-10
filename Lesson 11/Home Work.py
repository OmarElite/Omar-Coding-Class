class Shape:
    def area(self):
        print("Area: Not defined for base shape")

    def perimeter(self):
        print("Perimeter: Not defined for base shape")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area:", self.width * self.height)

    def perimeter(self):
        print("Perimeter:", 2 * (self.width + self.height))
        print()


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        print("Area:", 0.5 * self.base * self.height)

    def perimeter(self):
        print("Perimeter:", self.side1 + self.side2 + self.side3)
        print()


# Example usage
rectangle = Rectangle(4, 5)
rectangle.area()
rectangle.perimeter()

square = Square(4)
square.area()
square.perimeter()

triangle = Triangle(3, 4, 3, 4, 5)
triangle.area()
triangle.perimeter()
