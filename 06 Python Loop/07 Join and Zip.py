print("\n----- Use of Join module -----\n")
strS1 = "Sohag"
print("Before Join: ", strS1)
strS2 = '-'.join(strS1)
print("After Join: ", strS2)

print("\n----- Use of zip 01 -----\n")
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = []
for i in list1[0::2]:
    list2.append(i)
print(list2)  # Output: ['a', 'c', 'e']

list3 = []
for i in list1[1::2]:
    list3.append(i)
print(list3)  # Output: ['b', 'd', 'f']

print(list(zip(list2, list3)))

print("\n----- Use of zip 02 -----\n")
result = [i + j for i, j in zip(list1[::2], list1[1::2])]
print(result)
