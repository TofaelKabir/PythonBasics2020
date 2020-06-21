# In this program we will override the parent class' funct
# We will also see how to call the super class' constructor by using super()


class Father:  # Parent class
    # constructor
    def __init__(self):
        print("I am in Father class")


class Child(Father):  # Sub class---inherits Nokia class
    def __init__(self):
        super().__init__()  # to call the super class constructor
        # print("I am in Child class")


# create obj
s1 = Child()

# If we run the program we will see it will print "I am in Child class"-->means it overrides parent class init()
