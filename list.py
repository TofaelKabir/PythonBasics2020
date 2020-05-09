d1 = {}

d2 = {"Ankur": "Burger", "Arshad": "Fish",
      "Nasir": "Cars", "Jimmy": "Perfume",
      "Kaitlin": "Home",
      "Jenifer": {"A": "Kids", "B": "Burger", "C": "Chicken"},
      }
print(d2)
print(d2["Jenifer"])
d2["Moh"] = "Pizza"
d2["Vicky"] = "Cold"
d2["Rabia"] = "Kebabs"

# if "Ankur" in d2,
#     print("Yes, 'Ankur' is one of the keys in the d2 dictionary ")
#     print("Yes, 'Nasir' is one of the keys in the d2 dictionary ")

d3 = d2.copy()
print(d3)

