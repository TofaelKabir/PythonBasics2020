print("multi-line string:-----------------------------")
# use '''-----'''  or """------""" line will be printed as given in code
s = '''My name is Sohag
I live at woodside, NY, USA.
My neighbourhood is really very convenient to live at'''

print(s)

print("#**concept of String are Arrays------------------")

# Strings are Arrays-->strings in Python are arrays of bytes representing unicode characters.
# In python there is not char type-->a single character of a string is a string with length of 1

# we can use [] and index in it to access element of the sting
s = "Sohag"
print("s[0] =", s[0])

print("#Slicing(Partial String)---------------------------")
# -->return a range of characters by using the slice syntax.

print("s[0:3] =", s[0:3])  # Soh    0 to 2 index

# Negative Indexing-->negative indexes to start the slice from the end of the string:
print(s[-1])
# s[0]="S" s[1]="o" s[2]="h" s[3]="a" s[4]="g"
# s[-1]="g" s[-2]="a" s[-3]="h" s[-4]="0" s[-5]="S"

print(s[-5])  # S
print(s[0])  # S
print(s[0:3])  # Soh   [3] exclude-->upper boundary excluded
print(s[-3:-1])  # ha   [-1] exclude-->upper boundary excluded

print("s[-3:-1] =", s[-3:-1])  # ha  --> -1 will be excluded

print("#Some String functions:----------------------------")
# strip() method removes any whitespace from the beginning or the end

s1 = "     My Name Is Sohag     "  # white space at the begining and at the ending
print(s1)
print("strip():", s1.strip())  # My Name Is Sohag--->removes

s = "My Name Is Sohag"

# lower() method returns the string in lower case and The upper() method returns the string in upper case
print("lower()", s.lower())  # my name is sohag
print("casefold():", s.casefold())  # my name is sohag
print("upper()", s.upper())  # MY NAME IS SOHAG

# replace() method replaces a string with another string
m = "My Name Is Nonir"  # "My Game is Gonir"

print("replace():", m.replace("N", "G"))  # will replace all N to G

# split() method splits the string into substrings if it finds instances of the separator
# s=['My', 'Name', 'Is', 'Sohag']
x = s.split(" ")
print("split():", x)  # ['My', 'Name', 'Is', 'Sohag']  # so now strings are splitted into 4 indexes
print("x[0]:", x[3])  # Sohag

print("#Check String------------------------")
# To check if a certain phrase or character is present in a string,-->we can use the keywords in or not in.

txt = "My name is Sohag"
x = "Sohag" in txt
print("String is available:", x)  # True

y = "Orfat" not in txt
print("String is not available:", y)  # True

z = "Orfat" in txt
print("String is available:", z)  # False

print("# String Concatenation:---------")
a = "Hellow"
b = "World"
print("concatenation:" + a + b)

print("# String Format:------format()-------")
# we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where
# the placeholders {} are *** one or more arg

age = 41
phone = 3474005813
sentance = "I am {} and my phone number is {}"
print(sentance.format(phone, age))  # I am 41 and my phone number is 3474005813

# can be used index number to be placed in correnct placeholder
sentance1 = "The phone number {1} belongs to Sohag. His age is {0}"
print(sentance1.format(age, phone))

print("#Escape Character: \   --------------------")
# we use backslash to skip coming up char or special char  ->for example "" inside ""
# text="The team "Versilona" is my favorite"  #-->we are not allowed to write this way
text = "The team \"Versilona\" is my favorite"
print(txt)
# tex1='It's alright now' # not possible
tex1 = 'It\'s alright now'
print(tex1)
tex2 = "We can use \(backslash)"  # \ will not be printed it will be used to escape for next round bracket-->(
print(tex2)
print("without (\):", tex2)
tex3 = "We can use \\(backslash)"
print("with (\):", tex3)

# for new line we use \n
print("New\nLine")

# for Carriage Return we use \r
print("Carriage\rReturn")

# for tab we use \t
print("Tab\tTab")  # Tab Tab

# for Backspace we use \b
print("Back \bSpace")  # BackSpace

# for Form Feed we use \f
print("Form \fFeed")

## bellow codes__> I didnt understand----------------------------
# for Octal value we use \ooo
# A backslash followed by three integers will result in a octal value:
txt = "\150\105\154\154"
print(txt)  # Hellow

# for Hex value we use \xhh
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)
