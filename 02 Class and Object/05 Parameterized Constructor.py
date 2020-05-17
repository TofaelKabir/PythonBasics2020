# If we could pass the value while creating obj then we don't need to use function to set the value
class Employee:
    name = ""
    id = ""

    def __init__(self, Name, Id):  # creating constructor
        self.name = Name
        self.id = Id
# Unlike Java, we cannot define multiple constructors. However, we can define a default value if one is not passed
# If multiple constructor is present, then last one will be executed. see next file for it.
# https://www.javatpoint.com/python-constructors

    def display(self):
        print(f"Emp_Name: {self.name}, Emp_ID: {self.id}")


emp1 = Employee("Rajib", 505)
emp1.display()
print("---------------------------------")
emp2 = Employee("Kabir", 518)
emp2.display()
