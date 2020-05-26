# For a single user we can execute like this
id = 483
name = "Tofael"
gpa = 3.69
print(f"ID:{id}, Name:{name}, GPA:{gpa}")
print("............................................")


# For multiple user we can create Class
class Student:  # syntax of creating class, class name will be in Upper case
    id = ""
    name = ""
    gpa = ""


# In Java, Student st1 = new Student(); but here below --
st1 = Student()  # Creating an object of Students class
print("Is st1 a instance of Student class?")
print(isinstance(st1, Student))  # True if obj creation is ok
print("............................................")
st1.id = 484
st1.name = "Tanvir"
st1.gpa = 3.78
print(f"ID:{st1.id}, Name:{st1.name}, GPA: {st1.gpa}")
print("............................................")

st2 = Student()
st2.id = 488
st2.name = "Taufique"
st2.gpa = 3.56
print(f"ID:{st2.id}, Name:{st2.name}, GPA:{st2.gpa}")
print("............................................")

st3 = Student()
st3.id = 497
st3.name = "Faiyad"
st3.gpa = 3.89
print(f"ID:{st3.id}, Name:{st3.name}, GPA:{st3.gpa}")
