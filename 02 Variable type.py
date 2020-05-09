print("# 1 (String type 01, Presented by single or double quotation)\n")
name1 = "Mohammad"
name2 = 'T'
name3 = 'Kabir'
print(name1)
print(name2)
print(name3)
print(type(name1))
print(type(name2))
print(type(name3))
print(name1, name2, name3)
print(name1, end=" ")
print(name2, name3)
print(name1 + name2 + name3)
print("\n")

print("# 2 (String type 02, The way we will use)\n")
name = "Tofael"
print("My Name is: ", name)
print("Type of my Name is:", type(name))
print("\n")

print("# 3 (int type)\n")
age = 44
print("My age is: ", age)
print("Type of my age is:", type(age))
print("\n")

print("# 4 (floating type)\n")
grade = 3.9987
print("My grade is: ", grade)
print("Type of my grade is:", type(grade))
print("\n")

print("# 5 (boolean type 01)\n")
country1 = "USA"
country2 = "BD"
print("Is Country 1 and Country2 is same?", country1==country2)
print("Type is:", type(country1==country2))
print("\n")

print("# 6 (boolean type 02)\n")
print("When we use true/false, the type is: ", type(True))
print("\n")

print("# 7 (Combining few variables)\n")
print(name, age, grade)
print("My Name: ", name, ",Age: ", age, ",grade: ", grade)
# what is the mistake in below line? we can solve it by casting, see next file
# print("My Name: " + name + ",Age: " + age + ",grade: " + grade)
# print("My Name: " + name + ", Age: " + str(age) + ", grade: " + str(grade))
