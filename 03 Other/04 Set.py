s = set()
print(type(s))

s_from_list = set([1, 2, 3, 4])
print(s_from_list)
print(type(s_from_list))

s.add(5)
s.add(6)
s.add(7)
s1 = s.union({8, 9, 10})
print(s, s1)
s.remove(6)  # To remove
print(s)

# Adding multiple data in set by another set
s2 = {"a", "b", "c", "d"}
s.update(s2)
print(s)

# Adding single data
s.add("45")
s.add(45)
s.add("45")
s.add("45")
print(s)
s.discard("b")  # To discard
print(s)


