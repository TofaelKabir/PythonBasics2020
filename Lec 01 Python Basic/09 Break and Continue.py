print("------break---------")
i = 1
while i <= 12:
    if i == 8:  # when i==7 then break works otherwise it goes next step
        break
    print(i)
    i = i + 1  # i++
print("Last limit")

print("------continue---------")

for x in range(1, 20, 3):
    # print(x)
    if x % 2 != 0:  # skipping condition
        continue
    print(x)
