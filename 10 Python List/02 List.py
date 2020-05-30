from filecmp import cmp

print("\n----- Python List Built-in functions -----")
List01 = [8, 2, 7, 5, 1, 3, 5, 6, 4, 9]
List02 = [5, 2, 7, 8, 1, 3, 9, 6, 4, 5]
List03 = [1, 2, 3]
List04 = [1, 2, 3]

print(List01)
print(max(List01))
print(min(List01))

print("\n----- Use of list() -----")
aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)  # It converts any sequence to the list. Her tuple converts to List
print("List elements : ", aList)

print("\n----- Use of copy() -----")
evenlist = [6, 8, 2, 4]
copylist = []
copylist = evenlist.copy()
print("Original list:", evenlist)
print("Copy list:", copylist)
print("\n")

# Here, we are using list slicing concept to create a copy of the list. See the example below.
evenlist = [6, 8, 2]
copylist = []
copylist = evenlist[:]  # Copy all the elements
print("Original list:", evenlist)
print("Copy list:", copylist)
print("\n")

# he assignment operator can also be used to copy a list into another. This is most general approach but not recommended
evenlist = [6, 8, 2, 4, 10, 12]
copylist = []
copylist = evenlist  # Copy all the elements
print("Original list:", evenlist)
print("Copy list:", copylist)
print("\n")

even = [6, 8, 2, 4]  # Newly added
even.sort()
print(even)
even.sort(reverse=True)  # sort in reverse order
print(even)
print("\n")

# It returns empty list if the list is the list is empty. See the example below.
apple = []
apple.reverse()
print(apple)
print("\n")

apple = ['e', 'l', 'p', 'p', 'a']
apple2 = ['a', 'p', 'p', 'l', 'e']
apple.reverse()
if apple == apple2:
    print("Both are equal")
else:
    print("Not equal")

list = ['1', '2', '3']
for l in list:  # Iterating list
    print(l)
list.pop(2)

print("After poping:")
for l in list:  # Iterating list
    print(l)
# https://www.geeksforgeeks.org/python-2-number-cmplist-method/
# list1, list2 = [123, 'xyz'], [456, 'abc']
# print(cmp(list1, list2))
# print(cmp(list2, list1))
# list3 = list2 + [786]
# print(cmp(list2, list3))
# Not working
# print(cmp(List03, List04))
