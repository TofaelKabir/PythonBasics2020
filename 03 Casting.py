print("# 1 Why we need Casting\n")
a = '5'
b = '10'
print(a, b) # Any type of Variable is presenting side by side with a space, no concatenation
print(a+b) # Here is a complete concatenation without space for similar type of variable, here String + String

a = 5
b = 10
print(a, b)
print(a+b) # Here is a complete concatenation without space for similar type of variable, here int + int

a = 5
b = '10'
print(a, b)
# print(a+b)
# The above line is not working as int and String can't be concatenate
# We can solve this problem by casting
print("\n")

print("# 2 Use of Casting\n")
a = '5'
b = '10'
print(a, b)
print(int(a)+int(b))

a = '5.6'
b = '10.7'
print(a, b)
print(float(a)+float(b))   #why 16.299999999999997

a = 5
b = 10
print(a, b)
print(str(a)+str(b))

a = 5
b = '10'
print(a, b)
print(a+int(b))
print("\nWe can cast (int to String) and (String to int) by the above way")