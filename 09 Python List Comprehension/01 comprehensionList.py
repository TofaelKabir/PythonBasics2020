"""
List Comprehension is defined as an elegant way to define, create a list in Python and consists of brackets that contains
an expression followed by for clause. It is efficient in both computationally and in terms of coding space and time.
The list comprehension starts with '[' and ']'.
[ expression for item in list if conditional ]
"""
letters = []
for letter in 'Python':
    letters.append(letter)
print(letters)

letters = [letter for letter in 'Python']
print(letters)

x = {"Chrome": "browser",
     "Windows": "OS",
     "C": "language",
     }
print(x)  # Print all
print(x["Chrome"])  # Print ony Jenifer
print(x.get("C"))
x["mouse"] = "hardware"
print(x)
print(x["Windows"])
