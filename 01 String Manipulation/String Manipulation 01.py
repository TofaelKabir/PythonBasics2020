myName = "Subdermatoglyphic"
print(myName)
print(len(myName))  # length also include the space
# Why below one is true?
print(myName.isalnum())  # Return True if the string is an alpha-numeric string, False otherwise.
print(myName.isalpha(), "\n")  # Return True if the string is an alphabetic string, False otherwise

str1 = "HelloWorld123"
str2 = "HelloWorld"
str3 = "123"
str4 = "Hello World 123"
print(str1.isalnum())  # it means either alphabetical or numeric
print(str2.isalnum())
print(str3.isalnum())
print(str4.isalnum(), "\n")  # False -- because contain spaces, which is regarded as special

print(str3.isalnum())
print(str3.isnumeric())
print(str3.isdecimal())
print(str3.isdigit(), "\n")


print(myName.endswith("phic"))
print(myName.endswith("PHIC"))  # case sensitive
print(myName.startswith("Sub"))
print(myName.startswith("sub"))  # Case sensitive
print("\n")

print(myName.capitalize())  # Return More specifically, make the first character - upper case and the rest - lower case.
print(myName.upper())  # Return a copy of the string converted to uppercase.
print(myName.lower())  # Return a copy of the string converted to lowercase.
print(myName.count("y"))  # Return a copy of the string converted to uppercase.
print(myName.find("erm"))
""" S.find(sub[, start[, end]]) -> int
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  Optional arguments start and end are interpreted as in slice notation.
Return -1 on failure. """
print(myName.replace("phic", " many"))  # Return a copy with all occurrences of substring old replaced by new.

print(myName[0])  # Value at index 0
print(myName[1])  # Value at index 1
print(myName[2])
print(myName[3])
print(myName[15])
print(myName[-1])  # Value at index [length -1]
print(myName[-2])  # Value at index [length -2]
print(myName[-3])

print((myName[0:16]))  # 0 is initialized value and 16 is conditional value <16
print((myName[1:16]))
print((myName[2:16]))
print((myName[0:6]))
print((myName[4:11]))  # 4 is initialized value and 11 is conditional value <11
print((myName[0:25]))  # 0 is initialized value and 25 is conditional value <25, although the length is not 25
print((myName[6:25]))  # 6 is initialized value and 25 is conditional value <25, although the length is not 25

print(myName[::2])  # value present in index 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
print(myName[::6])  # value present in index 0, 6, 12, 18

print(myName[0:17:3])  # 0 is initialized value, 17 is conditional value <17, 3 is incremental value
# value present in index 0, 3, 6, 9, 12, 15
print(myName[0:17:2])  # 0 is initialized value, 17 is conditional value <17, 2 is incremental value
# value present in index 0, 2, 4, 6, 8, 10, 12, 14, 16. Similar like print(myName[::2])
