# 1: To comment out a line click command /
"""There is another way to comment out is by 3 double quotation"""
import datetime
print(datetime.datetime.now())

# 2
print("Hello World!")
print('Hey Python')
print(10 * "Hello World! ")

# 3 (how to Concatenate? 3 way. Which one is the best among first 2?)
print("Hello World!", "This is about Python")
print("Hello World!" + " This is about Python")

# 3 (Use of end parameter to Concatenate)
print("Hi!", "This is about Python.", end=" ")
print("I an using end feature here, it will concatenate the previous line ")

# 4 (use of next line by \n and tab by \t)
print("\nI am using next line by using backslash n.\nI am expecting it in next line")
print("\tI am using backslash t to get the tab option. \tDid you get it? \n\tCan't see the tab yet?")
print("\n")

# 5 (use of only \)
print("\'Tofael\'")  # only back slash tell the program to ignore the next symbol of it.
print('\"Tofael\"')
print('\'Tofael\'')
print("\"Tofael\"")
print("'Tofael'")  # Also possible this way
print('"Tofael"')

print("C:\Windows")
print("C:\'Windows'")

# 6(use of \r)
print('Hello Sir!\r 347-653-7214')  # using \r --> return carriage
