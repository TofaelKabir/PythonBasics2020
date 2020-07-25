"""
python data type -------->
text type: str
numeric type: int, float, (complex)
sequence type: list, tuple, (range)
mapping type: dict
set type: set, (forzenset)
boolean type: bool
binary type: (bytes, bytearray, memoryview)
"""

"""
Set --> data structure
    --> an unordered collection of items  ---> So we can't access value by index number
    --> No duplicate item/value allowed
"""
# ASCII TABLE

print("\n------------ Use of Set 01 ------------")
s = {56, 1, 78, 4, 1, 78, 34, 42, 2, 2}
print(s)
print(len(s))

print("\n------------ Use of add in Set 01 ------------")
s.add(56)
print(s)
s.add(54)
print(s)

print("\n------------ Use of remove in Set 01 ------------")
s.remove(2)  # remove even if it is duplicated
print(s)
print(type(s))

print("\n------------ Set membership ------------")
print(2 in s)  # False
print(56 in s)  # True

print("\n------------ Use of Set 02 ------------")
num1 = {1, 2, 3, 4, 5, 5}
print(num1)
print(type(num1))

print("\n------------ Use of Set() function------------")
num2 = set([4, 5, 6, 7, 8])  # How to turn a list to set -- by set() function helps to convert a list into set
print(num2)
print(type(num2))

num1 = {1, 2, 3, 4, 5, 5}
num2 = set([4, 5, 6, 7, 8])
print("\n ------------ After Using Union as a symbol in the set ------------")
# Union:--> symbol (|) is used ----> (common+uncommon)
print(num1 | num2)  # output->{1, 2, 3, 4, 5, 6, 7, 8}

print("\n ------------ Use of Intersection ------------")
# intersection->symbol: (&) --> only common
print(num1 & num2)  # output ->{4,5}

print("\n ------------ Use of difference ------------")
# difference --> symbol (-)---->remove common values from 1st set and print only rest of 1st set
print(num1 - num2)  # removes 4,5 -->output {1,2,3}

print("\n------------ Use of Set 03------------")
s = set()
print(s)
print(type(s))

# putting values in list then convert into set using set() function
s_from_list = set([4, 1, 3, 2])  # how to turn a list into set
print(s_from_list)
print(type(s_from_list), "\n")

s_from_list.add(7)
s_from_list.add(6)
s_from_list.add(5)
print(s_from_list)

print("\n ------------ After Using Union() function in the set ------------")
s1 = s_from_list.union({8, 9, 10})  # allow similar data type by union method
print(s1)
print(s_from_list, s1)

print("\n ------------ use of remove in the set ------------")
s_from_list.remove(6)  # To remove
print(s_from_list)

print("\n ----- we can Add different data type in set by another set -----")
s2 = {'a', 'b', 'c', 'd'}
s_from_list.union(s2)  # union doesn't allow different type of set addition, allow similar data type
print(s_from_list)
s_from_list.update(s2)  # update method is used to concatenate different data type in set
print(s_from_list, "\n")

print("\n ------ Adding single data in set 01 -------")
s_from_list.add('45')
# print("\n" + s_from_list)  # set ans string type can't concatenate
print(s_from_list)
print("\n ------ Adding single data in set 02 -------")
s_from_list.add(45)
print(s_from_list)
print("\n ------ Adding single data in set 03 -------")
s_from_list.add("45")
print(s_from_list)
print("\n ------ Adding single data in set 04 -------")
s_from_list.add("45")
print(s_from_list)
print("\n ------ Adding single data in set 05 -------")
s_from_list.add(1)
s_from_list.add(2)
print(s_from_list)  # duplicate data is not accepted in set as output

print("\n ------ Discard/remove single data in set 01-------")
s_from_list.discard('b')  # To discard
print(s_from_list)
print("\n ------ Discard/remove single data in set 01-------")
s_from_list.discard('a')  # To discard
print(s_from_list)
print("\n ------ Discard/remove single data in set 01-------")
s_from_list.discard('c')  # To discard
print(s_from_list)



