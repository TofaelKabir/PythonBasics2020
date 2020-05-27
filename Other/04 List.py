# List---> an obj of Python where we can store data

subject = ["C++", "Python", "Java", "Ruby", "C", "Java", "java"]  # we can store int, double, str together --->
# Here subject -- name of list
print(subject)  # to print the complete List
print(len(subject))
subject.reverse()  # Do the reverse of the value in List present
print(subject)
subject.reverse()  # Do the reverse of the value in List present
print(subject)
print("\n")

print(subject[0])  # to print the value in index [0]
print(subject[1])  # to print the value in index [1]
print(subject[2])  # to print the value in index [2]
print(subject[3])  # to print the value in index [3]
print(subject[4])  # to print the value in index [4]
print(subject[-1])  # to print the value in index [length-1]
print(subject[-2])  # to print the value in index [length-2]
print("\n")

# Initialized value, Start from mentioned index and print till end
print(subject[0:])  # to print value from index [2] to till end
print(subject[1:])  # to print value from index [2] to till end
print(subject[2:])  # to print value from index [2] to till end
print(subject[3:])  # to print value from index [2] to till end
print("\n")

# Conditional value, print value before that condition
print(subject[:0])  # to print value before index [0], so empty
print(subject[:1])  # to print value before index [1]
print(subject[:2])  # to print value before index [2]
print(subject[:3])  # to print value before index [2]
print("\n")

# to check the first position of the value if multiple is present
position = subject.index("Java")  # it will return as int for index value
print("Java is in:", position)

# to check number of occurrence
count = subject.count("Java")
print("Occurrence of Java:", count)  # Case sensitive
print("\n")

# to check element is available in list or not-->returns True/False
print("Python" in subject)  # True
print("swift" in subject)  # False
print("swift" not in subject)  # True
print("\n")

# to add more in our list
print(subject + ["swift"])  # It will be added as concatenate temporarily but not in list permanently
print(subject)
print("swift" in subject)  # False-->previous line actually didn't add in actual list-->need to use append() for adding
subject.append("swift")  # will be added at the last position
print("swift" in subject)  # this time it will show True
print(subject)
subject.insert(2, "Java Script")  # will be added in index [2] and previous items will be shifted to next position
print(subject)
print(len(subject))  # it will print the length of the list
print(subject * 2)  # It will print  the items twice
print(len(subject))  # it will print the length of the list
print("\n")

# to remove
subject.remove("java")  # remove() takes exactly one argument
print(subject, " & Length: ", len(subject))
subject.remove("Java")  # remove() takes exactly one argument and first one, when there is 2
print(subject, " & Length: ", len(subject))
print("\n")

# to sort, sorting is not possible if they are mixed of variable type like int, String etc
subject.sort()
print(subject)
subject.reverse()  # Do the reverse of the value in List present
print(subject)
subject.reverse()  # Do the reverse of the value in List present
print(subject)
print("\n")

# To copy and store in new list
subject2 = subject.copy()
print("After copying: ", subject2)

subject3 = ["C#", "PHP", "R"]
subject2.extend(subject3)
print("After extending: ", subject2)
print(subject3)
subject4 = ["PERL", "Scala"]
print("When we Concatenate subject4: ", subject2 + subject4)
print("After Concatenate: ", subject2)

# to clear the list items
subject2.clear()
print(subject2)  # []---no value
del subject3
# print(subject3) #-->will show not defined
