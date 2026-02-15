
from abc import ABC, abstractmethod
import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, w):
        self.width = w
    def set_height(self, h):
        self.height = h
    def get_area(self):
        area = self.width*self.height
        return area
    def get_perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter
    def get_diagonal(self):
        diagonal = math.sqrt((self.width**2) + (self.height**2))
        return diagonal
    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        else:
            width = "*"*self.width
            picture = self.height*(f"{width}\n")
            return picture
    def get_amount_inside(self, shape):
        amount = self.get_area()//(shape.get_area())
        return amount
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    def set_width(self, w):
        self.side = w
    def set_height(self, h):
        self.side = h
    def set_side(self, s):
        self.side = s
        self.width = s
        self.height = s
    def __str__(self):
        return f"Square(side={self.side})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

