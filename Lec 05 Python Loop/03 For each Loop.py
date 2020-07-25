myInfo = ["Tofael", 44, 3.999, "625W 57th st", "Mentor", 3476537214]
print(myInfo, "\n")

print("\n----- Use of For each Loop in the List 01 -----\n")
for i in myInfo:
    print(i)
print("\n")

print("\n----- Use of For each Loop in the List 02 -----\n")
for i in myInfo:  # after traversing value will be stored in i--->so we need to print i
    print(i, end="     ")

