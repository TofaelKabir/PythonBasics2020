"""
Some String Methods:
capitalize()Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()     Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()Sets the tab size of the string
find()	    Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	    Joins the elements of an iterable to the end of the string
ljust()	    Returns a left justified version of the string
lower()	    Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind() 	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	    Returns a right justified version of the string
rpartition()Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	    Splits the string at the specified separator, and returns a list
splitlines()Splits the string at line breaks and returns a list
startswith()Returns true if the string starts with the specified value
strip()	    Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	    Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	    Converts a string into upper case
zfill()	    Fills the string with a specified number of 0 values at the beginning """

print("\nUse of capitalize(), upper(), lower(), swapcase(), title(), casefold(), isupper(), islower(), istitle()\n")

txt = "Hello, and WELCOME you all."
# txt = "Hello, And Welcome You All."
print("capitalize():", txt.capitalize())
print("upper():", txt.upper())
print("lower():", txt.lower())
print("swapcase():", txt.swapcase())
print("title():", txt.title())
print("casefold():", txt.casefold())
print("isupper():", txt.isupper())
print("isupper():", txt.islower())
print("isupper():", txt.istitle())

print("\n----- Use of center() -- after how many space the word will start.-----")
txt = "banana"
print(txt.center(30))

print("\n----- Use of count() ----- Time of occurrence -----")
txt = "My name is Sohag. This name is very common in Bangladesh."
print(txt.count("name"))

print("\n----- Use of endswith() -----")
txt = "My name is Sohag."
print(txt.endswith("Sohag"))  # endswith(".") etc

print("\n----- Use of startswith() -----")
txt = "My name is Sohag."
print(txt.startswith("My"))

print("\n----- Use of expandtabs() --- how many spaces between tabs -----")
txt = "H\te\tl\tl\to"
x = txt.expandtabs(5)
print(x)

print("\n----- Use of find() --- to find the position of any letter or words-----------------------------")
# finds the first occurrence of the specified value.
# almost the same as the index()--But index() method raises an exception and find() returns -1 if not found
txt = "My name is Sohag"
x = txt.find("Z")
print(x)  # Will not throw Exception if it is absent

print("\n----- Use of index() --- to find the position of any letter or words")
txt = "My name is Sohag"
x = txt.index("S")
print(x)
# y = txt.index("Z")
# print(y)  # Will throw Exception if it is absent

print("\n----- Use of format() --- with fraction (f)--------------------")
txt = "Total cost is {price:.5f} dollars!"  # 2f-->.00, if 3f-->.00
print(txt.format(price=49))

print("\n----- Use of isdecimal() -----")
# True if all the characters are decimals (0-9).
# method is used on unicode objects.  (we can use the unicode chart)
txt = "0"
# txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

print("\n----- Use of join() -----")
myTuple = ("Sohag", "Orfat", "Sharif")  # Tuple is immutable and () is used instead of []
x = "*".join(myTuple)
print(x)

d2 = {"Ankur": "Burger",
      "Arshad": "Fish",
      "Nasir": "Cars",
      "Jimmy": "Perfume",
      "Kaitlin": "Home",
      "Jenifer": {"A": "Kids", "B": "Burger", "C": "Chicken"},
      }
y = "*  *".join(d2)  # d2 is a list here, will join the key, not the value
print(y)

s = {"Sohag", "Sharif", "Orfat"}
z = " *$* ".join(s)  # s is a set here
print(z)

print("\n----- Use of ljust() -----")
# Returns a left justified version of the string
txt = "S"
x = txt.ljust(5, "o")  # Total 5 including the txt, txt will be on most left then what you want to add
print(x)
print(x, "des ne.")
# left justified version of the word "Soooo" -->between first char "S" and next str "o"
# by default it will take space but we can use another arg instead of space-->x = txt.ljust(5,"#")--> Soooo des ne.

print("\n----- Use of rjust() -----")
# Returns a right justified version of the string
txt = "K"
y = txt.rjust(5, "O")  # Total 5 including the txt, txt will be on most right then what you want to add
print(y)
print(y, "Got it")
# right justified version of the word "OOOOK" -->between last char "K" and previous str "O"
# by default it will take space but we can use another arg instead of space-->Y = txt.rjust(5,"O")--> OOOOK Got it.

print("\n----- Use of lstrip(), rstrip() & strip() -----")
# lstrip() --> Returns a left trim version of the string
# rstrip() --> Returns a right trim version of the string
txt = "     Lobid     "
x = txt.lstrip()  # --> Remove spaces from the left side of the string
print("Among all", x, "is the best")
y = txt.rstrip()  # --> Remove spaces from the right side of the string
print("Among all", y, "is the best")
z = txt.strip()  # -->Remove spaces from left & right of the string
print("Among all", z, "is the best")

print("\n----- Use of partition() --- Take the first occurrence from multiple by default-----")
# searches for a specified string, and splits the string into a tuple containing three elements.
# 1 - before the "match"
# 2 - the "match"
# 3 - after the "match"

txt = "His name is Sharif. Mr. Sharif is a gentale man."
x = txt.partition("Sharif")
print(x)
y = txt.partition("His")
print(y)

print("\n----- Use of rpartition() --- Take the last occurrence from multiple by default-----")
z = txt.rpartition("Sharif")
print(z)
a = txt.rpartition("his")
print(a)

print("\n----- Use of zfill() -----")
# Fill the string with zeros until it is nth characters long
txt = "56"
x = txt.zfill(5)
print(x)  # 00056

# Can't understand it
print("\n----- Use of split(), rsplit() -----")
txt = "apple, banana, cherry"
x = txt.split(", ")
print(x)
y = txt.split("* ")
print(y)
y = txt.rsplit(", ")
print(y)

# Confused
print("\n----- use of splitlines() -----")
# Split a string into a list where each line is a list item:
# The splitting is done at line breaks.
txt = "Thank you all\nLet's start our session."
x = txt.splitlines()
print(x)

print("\n")
a = "Sohag"[0]
print(a)
b = "Sohag"[1]
print(b)
c = "Sohag"[2]
print(c)

print("----- Special Command shortcut --- to switch to prev by ctrl (^) E -----")
print("-------------------------------------")
