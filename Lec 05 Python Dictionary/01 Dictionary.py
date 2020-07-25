# dictionary is nothing but key value pairs, a dictionary is a collection of a unordered, changeable and indexed

d1 = {}  # Empty dictionary
print(d1)
print(type(d1))
d1['name'] = 'Tofael'
d1['age'] = 65
d1['sex'] = 'M'
print(d1['name'], d1['age'], d1['sex'], sep=' | ')
print(d1['name'], d1['age'], d1['sex'])


d2 = {"harry": "burger",
      "Arshad": "fish",
      "Nasir": "cars",
      "Jimmy": "perfume",
      "Kaitlin": "home",
      "jenifer": {"A": "kids", "B": "Burger", "C": "chicken"}
      }
print(d2)

d2["moh"] = "pizza"
d2["rabia"] = "kebab"
d2["vicky"] = "iphone"
print(d2)
print(len(d2))

if "jimmy" in d2:
    print("yes,'jimmy' is one of the keys in the d2 dictionary")
if "Jimmy" in d2:
    print("yes,'Jimmy' is one of the keys in the d2 dictionary")

# popitem() method remove last item
d2.popitem()
print(d2)  # Last one is popped up

# delete keys
del d2["jenifer"]  # key level delete
print(d2)
d2.update({"harry": "coffee"})  # Update the value of harry
print(d2)
d2.update({"moh": "pizza"})  # Update the value of harry
print(d2)
print(d2.get("harry"))
print(d2.get("moh"))

# copy of dictionary
d3 = d2.copy()
print(d3)

d4 = {"Nasir": "Kacchi",
      "Ahmed": "Roast Polao",
      "Shams": "Kacchi",
      "Tofael": "Kebab",
      }
print(d4)
d4.clear()  # clear will delete entire dictionary and give ana empty one
print(d4)

# delete full program
# del d2- will delete the dictionary and give an error
print(d2)
del d2
# print(d2)
# show error that's why comment out in above line





