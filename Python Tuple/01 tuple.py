"""
Tuple is another form of collection where different type of data can be stored.
It is similar to list where data is separated by commas. Only the difference is that list uses square bracket and tuple
uses parenthesis.
Tuples are enclosed in parenthesis and cannot be changed.
"""
from filecmp import cmp

print("\n----- Use of Tuple01 -----")
tp01 = ('Raven', 100, 60.4, 'Davis')
tp05 = (34, 190, 60.4, 56, 67, 87)
tp06 = (14, 190, 60, 6, 7, 87)
print(tp01)
print("Length of the tuple: ", len(tp01))
print("Maximum of the tuple: ", max(tp05))
print("Minimum of the tuple: ", min(tp05))

# print(cmp(tp05, tp06))  # Not working
# tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
# print(cmp(tuple1, tuple2))
# print(cmp(tuple2, tuple1))
# tuple3 = tuple2 + (786,)
# print(cmp(tuple2, tuple3))
# https://www.tutorialspoint.com/python/tuple_cmp.htm

print("\n")
aList = [123, 'xyz', 'zara', 'abc']
print("Printing the List: ", aList)
aTuple = tuple(aList)
print("List turned into Tuple elements : ", aTuple)

# tuple01 [1] = ['Sharif']
# TypeError: 'tuple' object does not support item assignment, it means no manipulation or changed in tuple

print("\n----- Tuple Indexing -----")
print(tp01[0])
print(tp01[1])
print(tp01[2])
print(tp01[-1])
print(tp01[-2])
print(tp01[-4])
# Like lists, the tuple elements can be accessed in both the directions. The right most element (last) of the tuple can
# be accessed by using the index -1. The elements from left to right are traversed using the negative indexing.

print("\n----- Tuple splitting  -----")
# It's include all: Initialized block, conditional block, incremental/decremental [+1] block
print(tp01[:])
print("\n")

# It's indicate Initialized block only, by default conditional block [<length, here<4], incr/decr [+1] block is applied
print(tp01[0:])
print(tp01[1:])
print(tp01[2:])
print(tp01[3:])
print("\n")

# It's indicate conditional block only, by default Initialization block [index 0], incr/decr [+1] block is applied
print(tp01[:4])
print(tp01[:3])
print(tp01[:2])
print(tp01[:1])
print("\n")

# It's indicate Initialized and conditional block, by default incr/decr [+1] block is applied
print(tp01[0:4])
print(tp01[0:3])
print(tp01[0:2])
print("\n")

print(tp01[1:4])
print(tp01[1:3])
print(tp01[1:2])
print("\n")

print(tp01[2:4])
print(tp01[2:3])
print(tp01[2:2])
print("\n")

print("\n----- Use of for loop in Tuple01  -----")
for i in tp01:
    print(i)

print("\n----- Use of Tuple02 -----")
tp02 = ("Sam", 10)
print(tp02)

print("\n----- Use of Tuple03 -----")
tp03 = (("Sohag", 41, "Woodside"), "Orfat", "Tofael")  # Tuple inside a tuple is possible
print(tp03)

print("\n----- Sum of Tuple -----")
tp = tp01 + tp02 + tp03
print(tp)

print("\n----- Use of for loop in sum of Tuple  -----")
for j in tp:
    print(j)

