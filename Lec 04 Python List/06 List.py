# 2D List or Matrix
'''
1 2 3 4 5
4 5 6 7 8
1 1 1 1 1
0 0 0 0 0
'''

# Nested list
matrix = [[1, 2, 3, 4, 5],
          [4, 5, 6, 7, 8],
          [1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0]
          ]

for x in matrix:
    for y in x:
        print(y, end=' ')
    print()
    # indentation

# List iteration by for loop
cars = ['honda', 'toyota', 'audi']
for car in cars:
    print(car)
    if car == 'toyota':
        print("My car is Toyota")
    if car == 'audi':
        print("My car is Audi")
    if car != 'volvo':
        print("Volvo Not in list")

# sum of list numbers
list_of_number = [1, 2, 3, 4, 5]
total = 0
for i in list_of_number:
    print(i)
    total += i  # or sum = sum +i
print("Total is {total}".format(total=total))

# sum of list numbers which contain String or float

list_of_number = [1, 2, 3, 4, 5, 'Bio', 2.345]
total = 0
for i in list_of_number:
    if type(i) == int:
        print(i)
        total += i  # or sum = sum +i
print("Total is {total}".format(total=total))