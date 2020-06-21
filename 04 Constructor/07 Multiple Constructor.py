# If we could pass the value while creating obj then we don't need to use function to set the value
class Employee:
    name = ""
    id = ""

    def __init__(self, Name, Id):  # creating constructor
        self.name = Name
        self.id = Id

    def display(self):
        print(f"Emp_Name: {self.name}, Emp_ID: {self.id}")

# HOW TO USE IT, ASK
emp1 = Employee("Tofael", 483)  # why can't use parameterized value?
emp1.display()
print("---------------------------------")
emp2 = Employee("Taufique", 488)
emp2.display()
