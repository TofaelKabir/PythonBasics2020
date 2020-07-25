print("..................................")
age = 24
print(age)  # 24

print("..................................")
age = 24 + 2
print(age)  #26

print("..................................")
age += 2.4
print(age)

print("..................................")
age -= 2.2
print(age)

print("..................................")
age *= 2
print(age)

print("..................................")
age /= 2
print(age)

print("..................................")
x = 10
print(x)
x = -x
print(x)

print("..................................")
# Use of Divmod
x = 11
y = 2

result1 = x / y
print(result1)  # 5.5

result2 = x // y
print(result2)  # 5

result3 = x % y
print(result3)  # 1

# new
result = divmod(x, y)
print(result)  # outcome as 5 and 1
print(result[0])
print(result[1])

x = 2
result5 = x ** 3
print(result5)

# new
result6 = pow(2, 4)  # power function
print(result6)

# Whitespace
name = "          Tofael          "  # whitespace
print('_*_' + name + '_*_')
print('_*_' + name.lstrip() + '_*_')
print('_*_' + name.rstrip() + '_*_')
print('_*_' + name.strip() + '_*_')
print('_*_' + name.lstrip().rstrip() + '_*_')  # Method chaining - one method after another

# Print separator
x = "NY"
y = "MD"
z = "NJ"
print(x + ' | ' + y + ' | ' + z)
print(x, y, z, sep=' | ')  # another way

# String interpolation
# old style
person = '%s\'s age is %d'  # need to know more
print(person % ('Bill', 55))

# New style
person = '{name}\'s age is {age}'
print(person.format(name='Bob', age=45))
print(person.format(name='Brian', age=35))

# Formatted String literal Python 3.6+
name = 'Michael'
age = 25
person = f'{name}\'s age is {age}'
print(person)
