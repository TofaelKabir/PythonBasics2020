# Python Polymorphism-->many forms

# Built in polymorphic function
print(len("Sohag"))  # len()---> is counting length of string
print(len([10, 20, 30, 40]))  # len()---> is counting length of  list


# user defined polymorphic function
def add(x, y, z=0):  # intention of z value--> if z value is passed then it counts 0
    return x + y + z


print(add(20, 30))  # as we pass two value then it will calculated 20+30+0=50
print(add(20, 30, 40))  # as we pass three value then it will calculated 20+30+40=90-->z value will be replaced by 40
