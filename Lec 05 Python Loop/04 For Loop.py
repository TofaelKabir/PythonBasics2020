myInfo = ["Tofael", 44, 3.999, "625W 57th st", "Mentor", 3476537214]
print("----- Use of for loop in the List 01 -----\n")
# initialization block, conditional block, incremental/decremental block
for i in range(0, 6, 1):
    print(myInfo[i])

print("\n----- Use of for loop in the List 02 -----\n")
num = [10, 20, 30, 40, 50, 60]
# sum by using for loop
total = 0
for i in num:
    total = total + i
print("Sum of all number: ", total)

print("\n----- Use of for loop in the List 03-----\n")
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = []
for i in list1[0::2]:
    list2.append(i)
print(list2)  # Output: ['a', 'c', 'e']

print("\n----- Use of for loop in the List 04-----\n")
list3 = []
for i in list1[1::2]:
    list3.append(i)
print(list3)  # Output: ['b', 'd', 'f']
