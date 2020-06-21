# There is an attachment(MagicMethods.docx) plz check
# Magic Method--> syntax:   _name_()
# Don't need to call Magic Method


class Bike:
    int = 5

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Name:{self.name},Color:{self.color}"

    def __eq__(self, Sharif):
        return self.name == Sharif.name and self.color == Sharif.color

    def __add__(self, ):
        return self.int \
               # + other

    # def display(self):
    #     print(f"Name:{self.name},Color:{self.color}")


bike1 = Bike("Pulsar", "Black")
# Print obj value by using display method-->common practice
# bike1.display()


# If we print obj without Magic Method
print(bike1.__add__())  # It will reuturn name of the obj <__main__.Bike object at 0x0101C178>

# If we use Magic Method-->__str__(self) then without display() we can print the obj value
# print(bike1) #-->Name:Pulsar,Color:Black

# If we compare the two obj of Bike class:
# bike2=Bike("Pulsar","Black")
# print(bike1==bike2) # Without Magic Method it will compare obj to obj but with Magic Method: __eq__(self, other)
