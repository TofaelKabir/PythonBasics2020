# If we could pass the value while creatiing obj then we dont need to use function to set the value

# creating class


class Employees:
    name = ""
    id = ""

    # creating constructor
    def __init__(self, name):
        self.name = name
        self.id = id

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Employee_Name:{self.name},Employee_ID:{self.id}")


emp1 = Employees("Moniruzzaman Monir", 505)
emp1.display()
print("---------------------------------")
emp2 = Employees("Mohammad Sharif", 506)
emp2.display()
