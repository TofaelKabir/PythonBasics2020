# List---> an obj of Python where we can store data

print("\n----- Use of List -----")
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]  # we can store int, double, str together --->
# Here subject -- name of list
print(language)  # to print the complete List
print(len(language))  # It is used to get the length of the list
language.reverse()  # Do the reverse of the value in List present
print(language)
language.reverse()
print(language)

print("\n----- Iterating a List by for loop  -----")  # The for loop is used to iterate over the list elements.
for i in language:
    print(i)

print("\n----- List Indexing -----")
print(language[0])  # to print the value in index [0]
print(language[1])  # to print the value in index [1]
print(language[2])  # to print the value in index [2]
print(language[3])  # to print the value in index [3]
print(language[4])  # to print the value in index [4]
print(language[-1])  # to print the value in index [length-1]
print(language[-2])  # to print the value in index [length-2]
# Like lists, the tuple elements can be accessed in both the directions. The right most element (last) of the tuple can
# be accessed by using the index -1. The elements from left to right are traversed using the negative indexing.

print("\n----- List splitting  -----")
# It's include all: Initialized block, conditional block, incremental/decremental [+1] block
print(language[:])
print("\n")

# It's indicate Initialized block only, by default conditional block [<length, here<6], incr/decr [+1] block is applied
print(language[0:])
print(language[1:])
print(language[2:])
print(language[3:])
print("\n")

# It's indicate conditional block only, by default Initialization block [index 0], incr/decr [+1] block is applied
print(language[:4])
print(language[:3])
print(language[:2])
print(language[:1])
print("\n")

# It's indicate Initialized and conditional block, by default incr/decr [+1] block is applied
print(language[0:4])
print(language[0:3])
print(language[0:2])
print("\n")

print(language[1:4])
print(language[1:3])
print(language[1:2])
print("\n")

print(language[2:4])
print(language[2:3])
print(language[2:2])
print("\n")

# to check the first position of the value if multiple is present
# It returns the lowest index in the list that object appears.
# The method returns index of first element occurred, if the element is duplicate.
position = language.index("Java")  # it will return as int for index value
print("Java is in:", position)

# Apart from element, the method takes two more optional parameters start and end.
# These are used to find index within a limit.
position = language.index("Python", 1)  # start index [1]
print("Python is in:", position)

position = language.index("Ruby", 1, 7)  # start index [1], End index [7]
print("Ruby is in:", position)

# The index() method throws an error ValueError if the element is not present in the list.
# position = language.index("Bye")  # it will return as int for index value
# print("Bye is in:", position)

# It returns the number of occurrences of the specified object in the list.
count = language.count("Java")
if count >= 2:
    print("value is duplicate")
print("Occurrence of Java:", count)  # Case sensitive
print("\n")

count = language.count("Hi")
print("Occurrence of Hi:", count)  # Case sensitive
print("\n")

# Membership: It returns true if a particular item exists in the List otherwise false.
print("Python" in language)  # True
print("swift" in language)  # False
print("swift" not in language)  # True

print("\n----- Adding elements to the list -----")
print("\n----- Updating List values by Concatenate -----")
print(language + ["swift"])  # Concatenation: It concatenates the list mentioned on either side of the operator.
print(language)
print("swift" in language)  # False-->previous line actually didn't add in actual list-->need to use append() for adding

print("\n----- Updating List values by append() -----")
language.append("swift")  # will be added at the last position
print("swift" in language)  # this time it will show True
print(language)

# Appending a list to the list is also possible which will create a list inside the list
list5 = ['4', '5', '6', '7']
language.append(list5)
print("List after appending element : ", language)
list5.append([23, 34])
print("List after multiple appending element : ", language)
# Appending multiple lists to the list will create a nested list.
# Here, two lists are appended to the list and generates a list of lists.

print("\n----- Updating List values by insert() -----")
# The object is inserted into the list at the specified index.
language.insert(2, "Java Script")  # will be added in index [2] and previous items will be shifted to next position
print(language)
print(len(language))  # it will print the length of the list
print(language * 2)  # Repetition: The repetition operator enables the List elements to be repeated multiple times.
print(len(language))  # it will print the length of the list
print("\n")

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

print("\n----- Updating List values by replacing -----")
print(language)
language[1] = 'TypeScript'  # This is replacing in a specific place
print(language, " & Length: ", len(language))
language[8] = 'Elixir'  # This is replacing in a specific place
print(language, " & Length: ", len(language))
language[4:7] = ['Kotlin', 'Rust', 'Java', 'Haskell']  # This is replacing from 4 to 6 place in previous list by new one
print(language, " & Length: ", len(language))

print("\n----- Updating List values by remove() -----")  # Newly added
print("Before removal: ", language, " & Length: ", len(language))
# It removes the specified object from the list.
# If list contains duplicate elements, the method will remove only first occurred element.

language.remove("java")  # remove() takes exactly one argument
print("After removal: ", language, " & Length: ", len(language))

language.remove("Java")  # remove() takes exactly one argument and first one, when there is 2
print("After removal: ", language, " & Length: ", len(language))

# language.remove("Tofael")
# If we remove an element which is not found in the list, it throws an error to the console
# print("After removal: ", language, " & Length: ", len(language))

print("\n----- Updating List values by pop() -----")  # Newly added
print("Before poping:", language)
language.pop()  # Last one is popped up
print("After poping:", language)
print("\n")

print("Before poping:", language)
language.pop(0)  # index [0] is popped up
print("After poping:", language)
print("\n")

print("Before poping:", language)
language.pop(-3)  # index [0] is popped up
print("After poping:", language)
print("\n")

print("\n----- Updating List values by deleting from position -----")  # Newly added
print("Before delete: ", language, " & Length: ", len(language))
del language[2]
print("After delete: ", language, " & Length: ", len(language))

print("\n----- Use of sort() -----")
# It sorts the list by using the specified compare function if given.
# to sort, sorting is not possible if they are mixed of variable type like int, String etc
# print("Before sort: ", language, " & Length: ", len(language))
# language.sort()
# print("After sort: ", language, " & Length: ", len(language))  # Newly added
# language.sort(reverse=True)
# print("After sort: ", language, " & Length: ", len(language))
# language.reverse()  # Do the reverse of the value in List present
# print("After reverse: ", language, " & Length: ", len(language))
# language.reverse()  # Do the reverse of the value in List present
# print("After Reversing again: ", language, " & Length: ", len(language))
# print("\n")

print("\n----- Use of copy(), extend() -----")
language1 = language.copy()
print("After copying: ", language1)

language2 = ["C#", "PHP", "R"]
print(language2)

language1.extend("abc")
print(language1)  # why abc is coming as a, b, c?

# It can be possible that the element is a tuple type and the list extends itself by tuple elements.
tuple1 = ('4', '5', '6')
language1.extend(tuple1)

# It can be possible that the element is a Set type and the list extends itself by Set elements.
set1 = {'7', '8', '9'}
language1.extend(set1)

# The sequence represented by the object seq is extended to the list.
language1.extend(language2)
print("After extending: ", language1)
language3 = ["PERL", "Scala"]
print("When we Concatenate language3: ", language1 + language3)
print("After Concatenate: ", language1)

print("\n----- Use of clear(), del -----")
language1.clear()
print(language1)

language1.clear()
print(language1)
# If the list is already empty, the method returns nothing.

language6 = []
language6.clear()
print(language6)  # []---no value


del language2
# print(subject3) #-->will show not defined
