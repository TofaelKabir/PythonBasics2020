# If we could pass the value while creating obj then we don't need to use function to set the value
class Employee:
    name = "Tofael"
    id = 483

    def __init__(self):  # creating constructor
        print("Printing from default constructor. Default constructor is initialized when class is instantiate")

    def display(self):  # method creation
        print(f"Emp_Name: {self.name}, Emp_ID: {self.id}")


emp1 = Employee()  # default constructor initialized here
print("---------------------------------")
emp1.display()
print("---------------------------------")
