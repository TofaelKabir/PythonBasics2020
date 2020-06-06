# Method Overriding-->using func from parent class with same name but changing the value

# In this program we will, after inheritance child class automatically get access the constructor
# when we will create the obj means we will call the constructor
# we will pass keyword to avoid the restriction to create fun/cons in class
# Parent class


class Nokia:  # Parent Class
    def __init__(self):  # constructor
        print("I am in Nokia class")


class Samsung(Nokia):  # Sub class Samsung is inheriting Nokia class
    pass  # You need to create at lease one func/cons--->to avoid we used pass


# create obj
s1 = Samsung()
# there is no constructor of Samsung class but it is printing because it is inheriting Parent class
