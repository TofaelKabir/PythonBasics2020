# Calculate the factorial of a given number

ex: 7 = 7 * 6 * 5 * 4 * 3 * 2 * 1


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


# Every module is python has a special attribute called - __name__ attribute is set to - __main__
# When module run as main program, otherwise the value of __name__ is set to contain the name of the module

if __name__ == '__main__':
    number: int = int(input("Enter a number: "))
    fac = factorial(number)
    print(f"The factorial is {fac}")
