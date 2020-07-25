num = 3

if num >= 3 and num < 5:
    print('3 to 5')
# or
if 3 <= num < 5:
    print('3 to 5')

name1 = 'Mohammad'
name2 = 'mohammad'

if name1.lower() == name2.lower():
    print("\nSame Name by lower method")

if name1.upper() == name2.upper():
    print("\nSame Name by upper method")

if name1 != 'Sharkar':
    print(name1)

if name1 != 'Mohammad':  # Not printing anything
    print(name1)
