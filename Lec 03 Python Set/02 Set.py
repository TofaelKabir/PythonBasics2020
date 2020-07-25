print("\n----- use of remove and discard method in set, similar function ------")
set1 = {"1", "2", "3"}
print(set1)
set1.remove("2")
print(set1)
set1.discard("3")
print(set1)

print("\n----- use of union method in set for similar type of data ------")
set2 = {"1", "2", "3", "4", "5"}
set3 = set1.union(set2)  # union is for similar data type
print(set3)

set4 = {7, 8}
print(set4)

set3.update(set4)  # for different data type
print(set3)
