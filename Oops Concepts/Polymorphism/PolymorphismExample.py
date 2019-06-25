# creating a shape Class
class Shape:
    width = 0
    height = 0

    # creating area method
    def area(self):
        print("Parent class Area ... ")


# creating a Rectangle Class
class Rectangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # overridding area method
    def area(self):
        print("Area of the Rectangle is : ", self.width*self.height)


# creating a Triangle Class
class Triangle(Shape):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    # overridding area method
    def area(self):
        print("Area of the Triangle is : ", (self.width*self.height)/2)


rectangle = Rectangle(10, 20)
triangle = Triangle(2,10)

rectangle.area()
triangle.area()

