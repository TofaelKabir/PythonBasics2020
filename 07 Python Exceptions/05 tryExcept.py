print("\n----- Why to Raise an exception -----")

# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:  # Why x>0 doesn't work
    raise Exception("Sorry, no numbers below zero")

'''Output: raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero'''


