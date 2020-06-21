"""
Set --> data structure
    --> an unordered collection of items->So we can't access value by index number
    --> No duplicate item/value allowed
"""

print("\n----- Use of Set 01 -----")
s = {56, 1, 78, 4, 1, 78, 34, 42, 2, 2}
s.add(56)
s.remove(2)  # remove even if it is duplicated
print(s)
print(type(s))
print(2 in s)  # False
print(56 in s, "\n")  # True

print("\n----- Use of Set 02 -----")
num1 = {1, 2, 3, 4, 5, 5}
num2 = set([4, 5, 6, 7, 8])
# Other Operations Union
# Union:--> symbol:(|)---->common+uncommon
print(num1 | num2)  # output->{1, 2, 3, 4, 5, 6, 7, 8}
# intersection->symbol: (&) -->only common
print(num1 & num2)  # output ->{4,6}
# difference --> symbol (-)---->remove common values from 1st set and print only rest
print(num1 - num2)  # removes 4,6 -->output {1,2,3}

print("\n----- Use of Set 03-----")
s = set()
print(type(s), "\n")
# putting values in list then convert into set using set() function
s_from_list = set([1, 2, 3, 4])
print(s_from_list)
print(type(s_from_list), "\n")


s_from_list.add(5)
s_from_list.add(6)
s_from_list.add(7)
s1 = s_from_list.union({8, 9, 10})
print(s_from_list, s1)
s_from_list.remove(6)  # To remove
print(s_from_list)

# Adding multiple data in set by another set
s2 = {"a", "b", "c", "d"}
s_from_list.update(s2)
print(s_from_list, "\n")

# Adding single data
s_from_list.add("45")
s_from_list.add(45)
s_from_list.add("45")
s_from_list.add("45")
s_from_list.add(1)
s_from_list.add(2)
print(s_from_list)  # duplicate data is not accepted in set
s_from_list.discard("b")  # To discard
print(s_from_list)


