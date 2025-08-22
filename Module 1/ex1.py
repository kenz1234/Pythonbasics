class Shape:
 def __init__(self,rectangle, circle):
     self.rectangle = rectangle
     self.circle = circle
class Rectangle(Shape):
 def __init__(self, length, width):
     self.length = length
     self.width = width

 def area(self):
     return self.length * self.width
 
class Circle(Shape):
 def __init__(self, radius):
     self.radius = radius

 def area(self):
     return 3.14 * self.radius * self.radius
 

x = Rectangle(5, 3)
y = Circle(4)

print("Area of Rectangle:", x.area())
print("Area of Circle:", y.area())