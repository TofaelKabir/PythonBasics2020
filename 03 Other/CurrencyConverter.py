with open('CurrencyConverter.txt') as f:
    lines = f.readlines()
    # print(lines)  # Printed in one line

    # for line in lines:
    #     parsed = line.split("\t")
    #     print(parsed)  # Printed line by line
    #     break

    # currencyDict = {}
    # for line in lines:
    #     parsed = line.split("\t")
    #     currencyDict[parsed[0]] = parsed[1]
    #     print(currencyDict)  # Printed line by line

    currencyDict = {}
    for line in lines:
        parsed = line.split("\t")
        currencyDict[parsed[0]] = parsed[1]

    amount = float(input("Enter amount:\n"))
    print("Enter the name of currency you want to convert this amount to? Available Option:\n")
    [print(item) for item in currencyDict.keys()]
    currency = input("Please enter of the value: ")
    print(f"{amount} Euro is equal to {amount*float(currencyDict[currency])}{currency}")
