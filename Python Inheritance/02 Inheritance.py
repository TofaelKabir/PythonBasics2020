class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print(" I am area method of shape class")


class Triangle(Shape):

    def area(self):
        area = 0.5 * (self.dim1 * self.dim2)
        area = 0.5 * (10 * 7)
        print("Area of Triangle:", area)


tr1 = Triangle(20, 20)
tr1.area()


#  Can't understand it
class Ractangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Ractangle:", area)


rt2 = Ractangle(20, 30)
rt2.area()
