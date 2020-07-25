print("# 1 All about List\n")

myInfo = ["Tofael", 44, 3.999, "625W 57th st", "Mentor", 3476537214]

print("The complete List: ", myInfo)
print("The length of the List is: ", len(myInfo))
print("3.999 is present in index: ", myInfo.index(3.999))

# print(myInfo.sort())  # sorting is not possible in a mixture of different data type

# MEMBERSHIP --
if "Tofael" in myInfo:
    print("\nYes, Tofael is present in the list")
elif "Tofael" not in myInfo:
    print("\nNo, Tofael is not present in the list")

myInfo = ["Tofael", 44, 3.999, "625W 57th st", "Mentor", 3476537214]
print("\nValue present in index 0 is: ", myInfo[0])
print("Value present in index 1 is: ", myInfo[1])
print("Value present in index 2 is: ", myInfo[2])
print("Value present in index 3 is: ", myInfo[3])
print("Value present in index 4 is: ", myInfo[4])
print("Value present in index 5 is: ", myInfo[5])
# print(myInfo[6])
print("Value present in index (length -1) is: ", myInfo[-1])
print("Value present in index (length -2) is: ", myInfo[-2])
print("Value present in index (length -3) is: ", myInfo[-3])
print("\n")

print("# 2 Use of for loop in the List\n")
for i in myInfo:
    print(i)
print("\n")

myInfo = ["Tofael", 44, 3.999, "625W 57th st", "Mentor", 3476537214]
print("# 3 Use of for loop with range in the List\n")
# initialization block, conditional block, incremental/decremental block
for i in range(2, 6, 1):
    print(myInfo[i])

number = [12, 1, 4, 5, 45, 67, 3, 5, 9]
print(number)
number.append(87)  # Added at the end
number.append(45)
number.append(-1)
print(max(number))
print(min(number))
print("After append: ", number)
number.reverse()
print("After Reverse: ", number)

number.sort()
print("After Sort: ", number)

number = [-1, 1, 3, 4, 5, 5, 9, 12, 45, 45, 67, 87]
print(number[:])
print(number[1:1])  # 1 is initialization, next 1 is condition <1, by default incremental/decremental is 1
print(number[1:2])  # 1 is initialization, next 2 is condition <2
print(number[1:3])  # 1 is initialization, next 3 is condition <2
print(number[0:3])  # 0 is initialization, next 3 is condition <3
