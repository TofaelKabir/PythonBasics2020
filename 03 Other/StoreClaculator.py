# Write a python program which will kepp adding a stream of numbers inputted by the user. The adding steps as an user
# press q key on the keyboard
total = 0
while True:
    userInput = input("Enter the price: \n")
    if userInput != 'q':
        total = total + int(userInput)
        print(f"Order total so far: {total}")

    else:
        print(f"Your bill total is {total}. Thank you for shopping with Walmart")
