print("\n----- Exception handling in python -----")
# Python provides the flexibility not to specify the name of exception with the except statement.

print("\n----- The except statement with no exception 01 -----")
y = 5
try:
    print(x)
except:
    print("An error handled for x")
print(y)

# when try block fails and raises error then control goes to except blocks and print "An error handled for x"
# Then control goes for other steps and print y value

print("\n----- The except statement with single exception 01 -----")
try:
    print(x)
except ArithmeticError:
    print("This is ArithmeticError")
except NameError:
    print("This is NameError")
else:
    print("No Errors occurred")

print("\n----- The except statement with single exception 02 -----")
try:
    print(x)
except ArithmeticError as ar:
    print(ar)  # It will print the error message from the console
except NameError as nr:
    print(nr)
else:
    print("No Errors occurred")

print("\n----- Use of Finally Block 01 -----")
try:
    print(x)
except NameError:
    print("name 'x' is not defined")
finally:
    print("Exception is handled")

# x variable is not defined-->try block raises error
# except block--> handled the exception and print message
# finally block--> executed regardless if the try block raises an error or not

print("\n----- A regular exception handling -----")
try:
    # this will throw an exception if the file doesn't exist.
    file1 = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    file1.close()

print("\n----- Use of Finally Block 02 -----")
try:
    myFile = open("fil.txt", "r")
    try:
        myFile.write("Hi I am good")
    finally:
        myFile.close()
        print("file closed")
except:
    print("Error")

print("\n----- Close objects and clean up resources--------")
try:
    f = open("Test.txt")
    f.write("Sharif is a quick learner")
except:
    print("file not found")
finally:
    print("Error")
