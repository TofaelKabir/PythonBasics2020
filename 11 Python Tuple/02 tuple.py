# https://www.javatpoint.com/python-tuples
tuple01 = (4, 8, 3)
tuple03 = (9, 2, 7)
print(tuple01)
print(tuple03, "\n")
# Repetition: The repetition operator enables the tuple elements to be repeated multiple times.
print(tuple01*2, "\n")
# Concatenation: It concatenates the tuple mentioned on either side of the operator.
print(tuple01 + tuple03, "\n")
# Membership: It returns true if a particular item exists in the tuple otherwise false.
print(4 in tuple01)
print(4 in tuple03)

print("\n----- Nesting List and tuple -----")
Employees = [(101, "Adam", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
print("\n----- Printing list -----")
for i in Employees:
    print(i)
Employees[0] = (110, "David", 22)
print("\n----- Printing list after modification -----");
for i in Employees:
    print(i)

tuple02 = (10, 20, 30, 40, 50, 60)
print(tuple02)
count = 0
for i in tuple02:
    print("tuple2[%d] = %d" % (count, i))  # Print the output is not right, need to fix the indexing

tuple02 = tuple(input("Enter the tuple elements ..."))  # doesn't work if we like to use double digit, even with coma
print(tuple02)
count = 0
for i in tuple02:
    print("tuple2[%d] = %s" % (count, i))
