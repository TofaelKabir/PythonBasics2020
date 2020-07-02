"""
 python data type:----
 text type: str
 numeric type: int, float, complex
 sequence type: list, tuple, range
 mapping type: dict
 set type:set, frozenset
 boolean type: bool
 binary type: bytes, byte array, memory view
 """
# Need to see them, didn't check yet
# Setting the Data Type:--->assign a value to a variable
# s = "Sohag"
i = 20
r = range(8)
print(r)  # range(0, 8)

t = (1, 2, 5, 6)  # tuple
d = {"name": "John", "age": 36}  # dict
set = {"Sohag", "Sharif", "Orfat"}  # set
fs = frozenset({"Sohag", "Sharif", "Orfat"})  # frozenset
b = b"Hello"  # byte
print(b)
ba = bytearray(2)  # bytearray
print(ba)  # bytearray(b'\x00\x00')
m = memoryview(bytes(5))
print(m)  # <memory at 0x00BC0BC8>

# Setting the Specific Data Type:--->using constructor func like str(), int() etc
s = str("Sohag")
print(s)  # Sohag
l = list([1, 5, 6, 8])
print(l)  # [1, 5, 6, 8]

# Python Numbers:
i = 20  # -->Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

f = 20.5  # float or "floating point number" is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3  # 35000.0 --->35 then 000 (after e it's 3)
y = 12E4  # 120000.0 --->12 then 0000
z = -87.7e100  # -8.77e+101 -->don't understand
print(x, y, z)  # 35000.0 120000.0 -8.77e+101

x = 20j  # Complex numbers are written with a "j" as the imaginary part
y = 10

print(x + y)  # (10+20j)--->still dont understand

# Type Conversion-->using constructor funct we can convert data type
# cannot convert complex numbers into another number type.

x = 10  # int
f = float(x)  # int--->to float
print(f)  # 10.0

x1 = int(f)  # float-->to int
print(x1)  # 10

c = complex(x1)  # int--->comlex
print(c)  # (10+0j)

# Random number generation:-->there is no random() but there is a bultin module: import it and use fuct like randrange()
import random

print(random.randrange(1, 5))  # will print any number btwn 1-5
print(random.randint(1, 5))  # will print any number btwn 1-5

# Casting-->using constructor func
# int() - constructs an integer number from an integer literal, a float literal (by rounding down to the
# previous whole number), or a string literal (providing the string represents a whole number)

b = int(2.8)  # b will be 2
c = int("3")  # c will be 3

# float() - constructs a float number from an integer literal, a float literal or a string literal
# (providing the string represents a float or an integer)
x = float(1)  # x will be 1.0
z = float("3")  # z will be 3.0

# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
