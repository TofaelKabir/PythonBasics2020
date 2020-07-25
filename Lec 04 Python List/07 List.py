print("\n----- Use of List -----")
language = ["java", "C++", "Python", "Java", "Ruby", "C", "Java", "java"]  # we can store int, double, str together --->
print(language)  # to print the complete List
print(len(language))  # It is used to get the length of the list

language[0] = "flutter"  # replacing the position
print(language)
print(len(language))

language.append("Javascript")  # add at the end
print(language)
print(len(language))

# language = language + ["Dart"]
language += ["Dart"]  # shortcut to add at the end
print(language)
print(len(language))

language.insert(2, "R")  # shortcut to add at the end
print(language)
print(len(language))

# splitting String into List items
# We need to import the re library for  that

import re

cars = "toyota, honda, bmw, audi"
car_list = re.split(',', cars)
print(car_list)


print(sorted(car_list))  # doesn't affect original list
print(car_list)


# List's string item concatenation
quote = ['Man', 'is', 'mortal']
print(quote)
quote_str = ' '.join(quote)
print(quote_str)


