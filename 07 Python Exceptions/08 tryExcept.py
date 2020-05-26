print("\n----- Raising exceptions 01 -----")
# An exception can be raised by using the raise clause in python. The syntax to use the raise statement is given below.
# Points to remember
# To raise an exception, raise statement is used. The exception class name follows it.
# An exception can be provided with a value that can be given in the parenthesis.
# To access the value "as" keyword is used. "e" is used as a reference variable which stores the value of the exception.
try:
    age = int(input("Enter the age?"))
    if age < 18:
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")

print("\n----- Raising exceptions 02 -----")
try:
    a = int(input("Enter a?"))
    b = int(input("Enter b?"))
    if b is 0:
        raise ArithmeticError
    else:
        print("a/b = ", a / b)
except ArithmeticError:
    print("The value of b can't be 0")

print("\n----- Custom exceptions 01 -----")
# The python allows us to create our exceptions that can be raised from the program and caught using the except clause.
# However, we suggest you read this section after visiting the Python object and classes.


class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    raise ErrorInCode(2000)
except ErrorInCode as ae:
    print("Received error:", ae.data)

