# List---> an obj of Python where we can store data

print("\n----- Use of List -----")
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]  # we can store int, double, str etc together
# Here language -- name of list
print(language)  # to print the complete List
print(len(language))  # It is used to get the length of the list
language.reverse()  # Do the reverse of the value in List present
print(language)
language.reverse()
print(language)

print("\n----- Iterating a List by for loop in list  -----")  # The for loop is used to iterate over the list elements.
for i in language:
    print(i)

print("\n----- List Indexing -----")
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print(language[0])  # to print the value in index [0]
print(language[1])  # to print the value in index [1]
print(language[2])  # to print the value in index [2]
print(language[3])  # to print the value in index [3]
print(language[4])  # to print the value in index [4]
print(language[-1])  # to print the value in index [length-1]
print(language[-2])  # to print the value in index [length-2]
# Like lists, the tuple elements can be accessed in both the directions. The right most element (last) of the tuple can
# be accessed by using the index -1. The elements from left to right are traversed using the negative indexing.

print("\n----- List splicing  -----")
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
# It's include all: Initialized block, conditional block, incremental/decremental [+1] block
print(language[:])
print("\n")

# It's indicate Initialized block only, by default conditional block [<length, here<6], incr/decr [+1] block is applied
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print(language[0:])
print(language[1:])
print(language[2:])
print(language[3:])
print("\n")

# It's indicate conditional block only, by default Initialization block [index 0], incr/decr [+1] block is applied
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print(language[:4])
print(language[:3])
print(language[:2])
print(language[:1])
print("\n")

# It's indicate Initialized and conditional block, by default incr/decr [+1] block is applied
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print(language[0:4])
print(language[0:3])
print(language[0:2])
print("\n")

language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print(language[1:4])
print(language[1:3])
print(language[1:2])
print("\n")

language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print(language[2:4])
print(language[2:3])
print(language[2:2])
print("\n")

# to check the first position of the value if similar value is present
# It returns the lowest index in the list that object appears if duplicated or more
# The method returns index of first element occurred, if the element is duplicate.
print("\n-------------- use of index() in list -------------------")
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java", 'dart']
position = language.index("Java")  # it will return as int for index value
print("Java is in position:", position)

# Apart from element, the method takes two more optional parameters start and end.
# These are used to find index within a limit.
position = language.index("Python", 1)  # start index [1]
print("Python is in:", position)

position = language.index("Ruby", 1, 7)  # between start index [1] and End index [7]
print("Ruby is in:", position)

position = language.index("java", 1, 8)  # between start index [1] and End index [7]
print("java is in:", position)

# The index() method throws an error -- 'ValueError' if the element is not present in the list.
# position = language.index("Bye")  # it will return as int for index value
# print("Bye is in:", position)

# It returns the number of occurrences of the specified object in the list.
count = language.count("Java")

if count >= 2:
    print("value is duplicated")
else:
    print("Not duplicated")

print("Occurrence of Java:", count)  # Case sensitive
print("\n")

language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java", 'dart']
count = language.count("Hi")
print("Occurrence of Hi:", count)
print("\n")

print("\n----- Membership in list -----")
# Membership: It returns true if a particular item exists in the List otherwise false.
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]
print("Python" in language)  # True
print("swift" in language)  # False
print("swift" not in language)  # True

language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java", 'dart']
print("\n----- Adding elements to the list -----")
print("\n----- Updating List values by Concatenate -----")
print(language + ["swift"])  # Concatenation: It concatenates the list mentioned on either side of the operator.
print(language)
print("swift" in language)  # False-->previous line actually didn't add in actual list-->need to use append() for adding

language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java", 'dart']
print("\n----- Updating List values by append() -----")
language.append("swift")  # will be added at the last position
print(language)
print("swift" in language)  # this time it will show True

language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java", 'dart']
# Appending a list to the list is also possible which will create a list inside the list
list5 = ['4', '5', '6', '7']
language.append(list5)
print("\nList after appending element : ", language)
list5.append([23, 34])
print(list5)
print("List after multiple appending element : ", language)
# Appending multiple lists to one list will create a nested list.
# Here, two lists are appended to the language list and generates a list of lists.

print("\n----- Updating List values by insert() -----")
language = ['java', 'C++', 'Python', 'Java', 'Ruby', 'C', 'Java', 'java', 'dart', ['4', '5', '6', '7', [23, 34]]]
print(language)
# The object is inserted into the list at the specified index.
language.insert(2, "Java Script")  # will be added in index [2] and previous items will be shifted to next position
print(language)
print(len(language))  # it will print the length of the list
print(language * 2)  # Repetition: The repetition operator enables the List elements to be repeated multiple times.
print(len(language))  # it will print the length of the list
print("\n")

language = ['java', 'C++', 'Java Script', 'Python', 'Java', 'Ruby', 'C', 'Java', 'java', 'dart', ['4', '5', '6', '7', [23, 34]]]
language.insert(5, ['JAVA', 'DART', 'java'])
print(language)
print("\n")

# It is possible to insert a tuple as an element to the list.
language.insert(6, ('J', 'D', 'j'))
print(language)
print("\n")

# It is possible to insert a set as an element to the list.
language.insert(7, {5, 6, 7})
print(language)
print("\n")

print("\n----- Updating List values by replacing -----\n")
language = ['java', 'C++', 'Java Script', 'Python', 'Java', ['JAVA', 'DART', 'java'], ('J', 'D', 'j'), {5, 6, 7}, 'Ruby', 'C', 'Java', 'java', 'dart']
print(language, " & Length: ", len(language))
language[1] = 'TypeScript'  # This is replacing in a specific place
print(language, " & Length: ", len(language))
language[8] = 'Elixir'  # This is replacing in a specific place
print(language, " & Length: ", len(language))
language[4:7] = ['Kotlin', 'Rust', 'Java', 'Haskell']  # This is replacing from 4 to 6 place in previous list by new one
print(language, " & Length: ", len(language))

print("\n----- Updating List values by remove() -----")  # Newly added
language = ['java', 'TypeScript', 'Java Script', 'Python', 'Kotlin', 'Rust', 'Java', 'Haskell', {5, 6, 7}, 'Elixir', 'C', 'Java', 'java', 'dart']
print("Before removal: ", language, " & Length: ", len(language))
# It removes the specified object from the list.
# If list contains duplicate elements, the method will remove only first occurred element.

language.remove("java")  # remove() takes exactly one argument and first one, when there is 2
print("After removal: ", language, " & Length: ", len(language))

language.remove("Java")  # remove() takes exactly one argument and first one, when there is 2
print("After removal: ", language, " & Length: ", len(language))

# language.remove([2])  # not possible to remove by indexing
print(language)
# Remove the comment out
# language.remove("Tofael")
# If we remove an element which is not found in the list, it throws an error to the console
# print("After removal: ", language, " & Length: ", len(language))

print("\n----- Updating List values by pop() -----")  # Newly added
language = ['TypeScript', 'Java Script', 'Python', 'Kotlin', 'Rust', 'Haskell', {5, 6, 7}, 'Elixir', 'C', 'Java', 'java', 'dart']
print("\nBefore popping:", language)
language.pop()  # Last one is popped up if not specify
print("After popping:", language)
print("\n")

print("Before popping:", language)
language.pop(6)
# print("Who is popped up? : ", language.pop(0))  # index [0] is popped up
# print("Who is popped up? : ", language.pop(5))  # index [5] is popped up
print("After popping:", language)

print("\n")

print("Before poping:", language)
language.pop(-3)  # index [-3] is popped up
print("After poping:", language)
print("\n")

print("\n----- Updating List values by deleting from position -----")  # Newly added
print("Before delete: ", language, " & Length: ", len(language))
del language[2]
print("After delete: ", language, " & Length: ", len(language))

print("\n----- Use of sort() -----")
# It sorts the list by using the specified compare function if given.
# to sort, sorting is not possible if they are mixed of variable type like int, String etc
language = ['TypeScript', 'Java Script', 'Python', 'Kotlin', 'Rust', 'Haskell', 'Elixir', 'Java', 'java']
print("Before sort: ", language, " & Length: ", len(language))
language.sort()  # sort is done according to alphabet and by upper case first, then lower case
print("After sort: ", language, " & Length: ", len(language))  # Newly added

language = ['Elixir', 'Haskell', 'Java', 'Java Script', 'Kotlin', 'Python', 'Rust', 'TypeScript', 'java']
# language.sort()  # there is no change if we sort again
language.sort(reverse=True)
print("\nAfter sort: ", language, " & Length: ", len(language))

print("\n----- Use of reverse() -----")
language.reverse()  # Do the reverse of the value in List present
print("After reverse: ", language, " & Length: ", len(language))
language.reverse()  # Do the reverse of the value in List present
print("After Reversing again: ", language, " & Length: ", len(language))
print("\n")


print("\n----- Use of copy() -----")
language = ['java', 'TypeScript', 'Rust', 'Python', 'Kotlin', 'Java Script', 'Java', 'Haskell', 'Elixir']
language1 = language.copy()
print("\nAfter copying: ", language1)



print("\n----- Use of extend() -----")
language1.extend("abc")  # extend() takes exactly one argument
language1.extend('D')
language1.extend('123')
print(language1)  # why abc is coming as a, b, c?


# It can be possible that the element is a tuple type and the list extends itself by tuple elements.
tuple1 = ('4', '5', '6')
language1.extend(tuple1)
print(language1)

# It can be possible that the element is a Set type and the list extends itself by Set elements.
set1 = {'7', '8', '9'}
language1.extend(set1)
print(language1)

# The sequence represented by the object seq is extended to the list.
language2 = ["C#", "PHP", "R"]
language1.extend(language2)
print("After extending: ", language1)
language3 = ["PERL", "Scala"]
print("When we Concatenate language3: ", language1 + language3)
print("Without Concatenate: ", language1)

print("\n----- Use of clear(), del -----")
language1 = ['java', 'TypeScript', 'Rust', 'Python', 'Kotlin', 'Java Script', 'Java', 'Haskell', 'Elixir', 'a', 'b', 'c', 'D', '1', '2', '3', '4', '5', '6', '9', '7', '8', 'C#', 'PHP', 'R']
print(language1)
language1.clear()  # clear method clear the list
print(language1)
print(language)

language2.clear()
print(language2)
# If the list is already empty, the method returns nothing.

language6 = []  # empty list
language6.clear()
print(language6)  # []---no value

print(language3)
# del language3  # del parameter delete the list and can'r trace
print(language3)  # will show not defined or not traced
