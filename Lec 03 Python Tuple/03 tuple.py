"""
Unlike lists, the tuple items can not be deleted by using the del keyword as tuples are immutable.
To delete an entire tuple, we can use the del keyword with the tuple name.
"""
tuple = (1, 2, 3, 4, 5, 6, 'physics', 'chemistry', 1997, 2000)
# If we change tuple to tp, the whole execution doesn't work, need to check why?
print(tuple)
# del tuple[0]  # TypeError: 'tuple' object doesn't support item deletion
# print(tuple)
del tuple
print("-----------------------------------------")
print(tuple)  # See the outcome from this, not clear
print("-----------------------------------------")
print(type(tuple))  # See the outcome from this, not clear

"""
1. Using tuple instead of list gives us a clear idea that tuple data is constant and must not be changed.

2. Tuple can simulate dictionary without keys. Consider following nested structure which can be used as a dictionary.
[(101, "John", 22), (102, "Mike", 28),  (103, "Dustin", 30)]  
 
3. Tuple can be used as the key inside dictionary due to its immutable nature.
"""
