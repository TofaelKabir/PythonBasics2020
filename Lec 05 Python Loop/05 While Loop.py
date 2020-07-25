print("----- Use of While Loop 01 -----\n")
i = 1
while i < 5:
    print(i)
    i = i + 1  # we can also write i+=1

print("----- Use of While Loop 02 -----\n")
i = 0
while i <= 10:
    print(i)
    i = i + 2

print("----- Use of While Loop 03 -----\n")
# calculate the sum of all even numbers from 0-10
i = 0
total = 0
while i <= 10:
    total = total + i
    i = i + 2
print("sum of all even numbers:", total, "\n")

# sum of numbers
n = int(input("Enter the range of the loop: "))
total = 0
i = 1
while i <= n:
    total = total + i
    i = i + 1
print("sum of all even ad odd numbers:", total)

print("----- using while loop to traverse -----\n")
num = [10, 20, 30, 40, 50, 60]
print(num)
index = 0
length = len(num)
while index < length:
    print(num[index], end="      ")
    index = index + 1
# print("")  why this is put Shohag?

# Infinite loop, better stop while running
# x = 1
# while True:
#     print(x)
#     x += 1
# to solve this problem -
x = 1
while True:
    print(x)
    x += 1
    if x > 10:
        break

# sum 1 to 10
total = 0
for i in range(1, 11):
    print(i)
    total += i  # or sum = sum +i
print("Total is {total}".format(total=total))

# String characters by for loop
title = 'Macbook Air.'
for char in title:
    print(char)
