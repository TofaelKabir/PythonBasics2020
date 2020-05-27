d1 = {}  # What is the purpose of this?

d2 = {"Ankur": "Burger",
      "Arshad": "Fish",
      "Nasir": "Cars",
      "Jimmy": "Perfume",
      "Kaitlin": "Home",
      "Jenifer": {"A": "Kids", "B": "Burger", "C": "Chicken"},
      }

print(d2)  # Print all
print(d2["Jenifer"])  # Print ony Jenifer
print(d2.get("Ankur"))
# Adding data
d2["Moh"] = "Pizza"
d2["Vicky"] = "Cold"
d2["Rabia"] = "Kebabs"

# Update data
d2.update({"Ankur": "Chicken"})
print(d2)
print(d2.get("Ankur"))

# boolean value - data present or not
if "Ankur" in d2:
    print("Yes, 'Ankur' is one of the keys in the d2 dictionary ")
    print("Yes, 'Nasir' is one of the keys in the d2 dictionary ")

print(d2)
print(len(d2))  # to know the length

d2.popitem()  # Remove the last data
print(d2)
print(len(d2))  # to know the length

# Delete data
del d2["Jenifer"]
print(d2)
print(len(d2))  # to know the length

# New Dictionary
d3 = d2.copy()
print(d3)

# Another way of new dictionary
d4 = dict(d3)
print(d4)

# del d3  # To delete all
# print(d3)

d3.clear()
print(d3)
