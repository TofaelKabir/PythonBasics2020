# https://www.javatpoint.com/python-tuples
print("\n------------ Tuple ------------")
tuple01 = (4, 8, 3)
tuple03 = (9, 2, 7)
print(tuple01)
print(tuple03)

print("\n------------ Tuple Repetition ------------")
# Repetition: The repetition operator enables the tuple elements to be repeated multiple times.
print(tuple01 * 2)

print("\n------------ Tuple Concatenation ------------")
# Concatenation: It concatenates the tuple mentioned on either side of the operator.
print(tuple01 + tuple03, "\n")

print("\n------------ Tuple Membership ------------")
# Membership: It returns true if a particular item exists in the tuple otherwise false.
print(4 in tuple01)
print(4 in tuple03)

print("\n------------ Nesting List and tuple ------------")
Employees = [(101, "Adam", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
for i in Employees:
    print(i)

Employees[0] = (110, "David", 22)  # this is a LIst, list is mutable
print("\n------------ Printing list after modification ------------");
for i in Employees:
    print(i)

# not working
#
# print("\n------------ Use of count, not working, have to see again ------------")
# tuple02 = (10, 20, 30, 40, 50, 60)
# print(tuple02)
# count = 0
# for i in tuple02:
#     print("tuple2[%d] = %d" % (count, i))
#
# tuple02 = tuple(input("Enter the tuple elements ..."))  # doesn't work if we like to use double digit, even with coma
# print(tuple02)
# count = 0
# for i in tuple02:
#     print("tuple2[%d] = %s" % (count, i))
