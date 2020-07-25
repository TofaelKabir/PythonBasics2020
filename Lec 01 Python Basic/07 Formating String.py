num1 = 10
num2 = 15
print("sum of num1 and num2 is: ", num1 + num2, "\n")  # 25

# To print-->10+15=25
print(f"{num1}+{num2} = {num1 + num2}")  # f for formatted text, {} for internal cal
print(r"{num1}+{num2} = {num1 + num2}")  # r-->raw
# print(r"hOPE YOU UNDERSTAND RAW")
# print(f"hI i am going to add {num1}+{num2} = {num1 + num2}")
print(f"Add:{num1}+{num2} = Sum: {num1 + num2}")

# To print-->20+10=30
num3 = 20
num4 = 10
total = num3 + num4
print(f"{num3} + 10 = {total}")  # {} for internal cal of total  # question about output

# we don't need f if there is no internal value representation
print("20+10=30")  # just a str

# what is the use of r --->raw

# how to print without a  new line
print("Sohag", end=" ")
print(41)  # output: Sohag 41
