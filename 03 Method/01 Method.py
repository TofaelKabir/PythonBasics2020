# If we could pass the value while creating obj then we don't need to use function to set the value
class Employee:
    name = "Tofael"
    id = 483

    def display(self):  # method creation
        print(f"Emp_Name: {self.name}, Emp_ID: {self.id}")


emp1 = Employee()
print("---------------------------------")
emp1.display()
print("---------------------------------")
