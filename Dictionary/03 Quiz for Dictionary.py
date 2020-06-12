# create a dictionary and take input from the user and return the meaning of the word from the dictionary

word = input("Type your word what you are looking from dictionary: ")
dict1 = {"ankur": "teacher",
         "jimmy": "player",
         "john": "pizzaman",
         "pranti": "burger",
         "priyana": "lemonhead",
         "tofael": "cars",
         "Jimmy": "perfume",
         "Eva": "home",
         "jenifer": {"A": "kids", "B": "Burger", "C": "chicken"}
         }
print(dict1[word])
