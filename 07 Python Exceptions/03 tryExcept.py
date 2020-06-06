"""
---> The try block lets you test a block of code for errors.
---> The except block lets you handle the error.
---> The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

"""
A list of common exceptions that can be thrown from a normal python program is given below.
    ZeroDivisionError: Occurs when a number is divided by zero.
    NameError: It occurs when a name is not found. It may be local or global.
    IndentationError: If incorrect indentation is given.
    IOError: It occurs when Input Output operation fails.
    EOFError: It occurs when the end of the file is reached, and yet operations are being performed.
"""

print("\n----- The except statement with exception -----")
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = %d" % c)
except Exception:
    print("can't divide by zero")
else:
    print("Hi I am in else block")

print("\n----- The except statement with no exception -----")
try:
    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    z = x/y
    print("x/y = %r" % z)
except:
    print("can't divide by zero")
else:
    print("The except statement with no specific exception")
