# Python Dates-->is not a data type of its own
import datetime


print("\n## type-----------------------------------")
print(datetime.date)  # <class 'datetime.date'>

print("\n## display current date&time---------------")
x = datetime.datetime.now()
print(x)  # year, month, day, hour, minute, second, and microsecond
print(x.year)
print(x.month)
print(x.date())
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)

print("\n## display in different form --------------")
# There is a chart (in same dir)-->for specific formats. char in upper or lower and different char represents dif forms
print(x.strftime("%A"))
print(x.strftime("%a"))
print(x.strftime("%B"))
print(x.strftime("%c"))

print("\n## Creating Date Objects---------------")
'''To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.'''

x = datetime.datetime(2023, 5, 17)
y = datetime.datetime.now()
a = x.year
b = y.year
print("Starting time:", y)
print("diff:", a - b)
