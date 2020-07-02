print("------ Use of break in for loop ---------")
print("Before use of break the output is below:")
for a in range(1, 20, 3):
    print(a)
print("After use of break the output is below:")
for a in range(1, 20, 3):
    if a == 13:  # what happen if you put 12?
        break
    print(a)

print("\n------ Use of break in While loop ---------")
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i = i + 1
print("When break implemented, loop stop before that condition\n")

print("------Use of continue in for loop------")
print("Before use of continue the output is below:")
for x in range(1, 20, 3):
    print(x)
print("\nAfter use of continue the output is below:")
for x in range(1, 20, 3):
    if x % 2 == 0:
        continue
    print(x)
# Not working, have to see again  #Shohag
# print("\n------ Use of continue in While loop ---------")
# y = 1
# while y <= 10:
#     if y == 8:
#         continue
#     print(y)
#     y = y + 1
print("When condition is met, condition will skip and continue")
