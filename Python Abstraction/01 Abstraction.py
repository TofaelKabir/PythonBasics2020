from abc import ABC, abstractmethod

# abc: python file
# Abstract Base Class(ABC):
# ABC Helper class that provides a standard way to create an ABC using inheritance.


class Shape(ABC):

    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    # method declared:
    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    # method implemented
    def area(self):
        area = 0.5 * (self.dim1 * self.dim2)
        print("Area of Triangle:", area)


# creating obj of Triangle-->indirectly passing the value for Shape calss constructor
tr1 = Triangle(20, 5)
tr1.area()


class Ractangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Ractangle:", area)


rt2 = Ractangle(20, 30)
rt2.area()

# Note:Why do we use abstract class--> to use as a blue print / model
# To make a class Abstract ->need to write (ABC) with the class name like inheritance
# need to import ABC (Abstract Base Class) from abc module-->need to implement abstract method
# need to use annotation before method-->@abstractmethod
# sub class has to use (implement) abstract method--->gives body
# As Abstract has at least one abstract method so we can't create obj of it.
