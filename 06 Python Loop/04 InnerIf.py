# (1)
marks = 75
if marks >= 40:
    if marks >= 80:
        print("distinct")
    elif marks >= 75:
        print("Excellent")
    else:
        print("general")
else:
    print("Fail")

# (2)
num1 = 60
num2 = 70
num3 = -100

if num1 > num2:
    if num1 > num3:
        print("Num1", num1)
    else:
        print("Num3", num3)


elif num1 < num2:  # else:-->we could use else here too
    if num2 > num3:
        print("Num2", num2)
    else:
        print("Num3", num3)
