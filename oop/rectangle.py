import math

# 1. Calculating the area.
# 2. Calculating the perimeter.
# 3. Calculating the length of the diagonal.
# 4. Determining whether or not the rectangle is a square.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Width: {self.width}, Height: {self.height}"

    def area(self):
        return self.width*self.height 
        
    def perimeter(self):
        return 2*(self.width + self.height)

    def diagonal(self):
        return math.sqrt((self.width**2)+(self.height**2))

    def is_square(self):
        return (self.width == self.height)

r1 = Rectangle(4, 4)
print(f"Area is {r1.area()}m")
print(f"Perimeter is {r1.perimeter()}m")
print(f"Is a square {r1.is_square()}")
print(f"Diagonal is: {r1.diagonal():.2f}m")
