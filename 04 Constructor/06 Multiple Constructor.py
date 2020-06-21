# If we could pass the value while creating obj then we don't need to use function to set the value
class Employee:
    name = ""
    id = ""

    def __init__(self):  # creating constructor
        print("Printing from default constructor.")

    def __init__(self, Name, Id):  # creating constructor
        self.name = Name
        self.id = Id

    def __init__(self):  # creating constructor
        print("Printing to prove, last one is initialized")

# Unlike Java, we cannot define multiple constructors. However, we can define a default value if one is not passed
# If multiple constructor is present, then last one will be executed.
# to learn more -- https://www.javatpoint.com/python-constructors

    def display(self):
        print(f"Emp_Name: {self.name}, Emp_ID: {self.id}")


emp1 = Employee()  # why can't use parameterized value?
emp1.display()
print("---------------------------------")
emp2 = Employee()
emp2.display()
