# 1. Hierarchical , 2. Multi-level, 3. Multiple Inheritance

# Multi-Level


class A:
    def display(self):
        print("I am from A class")


class B(A):
    def display1(self):
        print("I am from B class")


class C(B):
    def display2(self):
        # super().display() # we can also call super class' method
        # super().display1() # we can also call super class' method
        print("I am from C class")


c1 = C()
c1.display()
c1.display1()
c1.display2()
