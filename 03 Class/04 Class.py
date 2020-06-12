"""
Unlike Java, you cannot define multiple constructors.
However, you can define a default value if one is not passed.
"""


class Students:
    id = ""
    name = ""
    gpa = ""

    # def __init__(self):
    #     print("default cons")

    def __init__(self, Id, name, gpa):
        self.id = Id
        self.name = name
        self.gpa = gpa
        print(Id, name, gpa)

    def display(self):
        print(self.id)


class Employees:
    pass


st1 = Students(505, "Lobid", 101)
st1.display()
print(isinstance(st1, Students))  # True if obj creation is ok
print("............................................")


