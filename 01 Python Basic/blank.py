# Dictionary--->data structure where we can store data in key value pair
# 1.
print("--------studentId-----------")
studentId = {
    "101": "Sohagh", "102": "Sharif", 103: "Orfat",  # key-int: value-String
}
print(len(studentId))
print(studentId["101"])  # single value
studentId.update({"101": "Sohag"})
print(studentId.get("101"))  # Sohag

print("--print all Key's value----")
for x in studentId:
    print(studentId[x])

print("------copy dic----------")
studentId2 = studentId.copy()
print(studentId2)

print("------using dict----------")
studentId3 = dict(studentId)
print(studentId3)

print("-----after adding--------")
studentId[106] = "Monir"  # Adding
studentId["Rahman"] = 109  # Adding
print(len(studentId))
print(studentId)

print("------after removing----------")
studentId.pop("Rahman")
print(studentId)
print(len(studentId))
studentId.popitem()
print(studentId)

print("------after deleting----------")
del studentId['101']
print(studentId)

# del studentId   # it will delete entire dictionary
# print(studentId)

print("------after clear----------")
studentId.clear()  # it will clear all data inside
print(studentId)

# 2.
employees = {"Sohag": {101, 102, 103}, "Orfat": {505, 605, 707}}
print(employees["Sohag"])
print("--------print using for loop--------")
for i in employees:
    print(employees[i])

# 3
print("#--------nested dictionary--------")
groupEmployees = {
    "emp1": {"Name": "Sohag", "ID": 101, "Dep": "IT"},
    "emp2": {"Name": "Orfat", "ID": 102, "Dep": "IT"},
    "emp3": {"Name": "Monir", "ID": 103, "Dep": "IT"},
}
print(groupEmployees)
print("-----------using looping------")
for x in groupEmployees:
    print(groupEmployees[x])
