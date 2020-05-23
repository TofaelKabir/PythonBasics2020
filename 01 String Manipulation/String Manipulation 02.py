# To see the type of the value

num = input("Enter your number: ")
print(type(num))  # <class 'str'>--> as we know input gives str
a = 5
b = 5
print(type(a == b))

num1 = 20
print(num1)
print(type(num1))  # <class 'int'>

num1 = 20.5
print(type(num1))  # <class 'float'>

num1 = 'tofayel'
print(type(num1))  # <class 'str'> actualy in python it is str

num1 = 20.6431313
print(type(num1))  # <class 'float'> actualy in python it is float

print(type(False))  # <class 'bool'>

# Formating String
num2 = 10
num3 = 15
print("sum of num2 and num3 is: ", num2 + num3)  # 25

# To print-->10+15=25
print(f"{num2} + {num3} = {num2 + num3}")  # f for formated text, {} for internal cal, + or = for dir print  r-->raw
print(f"Add:{num2}+{num3} = Sum: {num2 + num3}")
# To print-->20+10=30
num4 = 20
num5 = 10
sum = num4 + num5
print(f"{num4} + 10 = {sum}")  # {} for internal cal of sum

# we dont need f if there is no internal value representation
print("20+10=30")  # just a str

# how print without a  new line
print("Sohag", end=" ")
print(41)  # output: Sohag 41
