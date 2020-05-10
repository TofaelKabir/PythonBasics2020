myName = "SUBDERMATOGLYPHIC"
print(myName)
print(len(myName))  # length also include the space

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


print(myName[::6])