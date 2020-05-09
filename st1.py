thisSet1 = {"1", "2", "3"}
print(thisSet1)
thisSet1.remove("2")
print(thisSet1)
thisSet1.discard("3")
print(thisSet1)

thisSet2 = {"1", "2", "3", "4", "5"}

thisSet3 = thisSet1.union(thisSet2)
print(thisSet3)

thisSet4 = {"7", "8"}
print(thisSet4)

thisSet3.update(thisSet4)
print(thisSet3)
