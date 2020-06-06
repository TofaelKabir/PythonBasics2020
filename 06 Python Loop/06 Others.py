# Double looping at same traversing action
# Need to do:Consecutive pair-->['ab', 'cd', 'ef']
print("\n----- ******************* 01 ********************* -----\n")
listS = ["sohag", "Orfat", "Lobid", "Tofael", "Manir", "Sharif"]
# traverse from 0 index and every 2nd indext store in a new list and print it
# Intend to traverse and store in a new list while staying inside the list
length = len(listS)
listR1 = [x for x in listS[0:length:1]]  # List comprehension
listR2 = [x for x in listS[0::1]]  # List comprehension
listR3 = [x for x in listS[0:length:2]]  # List comprehension
listR4 = [x for x in listS[0::2]]  # List comprehension
listR5 = [x for x in listS[::]]  # List comprehension
listR6 = [x for x in listS[2:5:1]]  # List comprehension
print(listR1)
print(listR2)
print(listR3)
print(listR4)
print(listR5)
print(listR6)
"""
listR=[x for x in listS[0::2]] --> inside the list: 1st x is iteration result (First x means, return of x)
As it is a looping syntax. Everything is in [], because it is stored in a list at the same time 
Finally list assigned to list var listR.
"""

print("\n----- ******************* 02 ********************* -----\n")
listX = []
for x in listS[::2]:
    listX.append(x)
print(listX)  # Output:['sohag', 'Lobid', 'Manir']


print("\n----- ******************* 03 ********************* -----\n")
for i in listS:
    print(i)

print("\n----- ******************* 04 ********************* -----\n")
print([i for i in listS])  # Alternative of above line

