print("\n----- Why to Raise an exception -----")
x = int(input("Enter a number: "))
print(x)
if x > 8:
    raise Exception("The condition is not true")

