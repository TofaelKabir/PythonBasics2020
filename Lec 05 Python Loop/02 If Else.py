# Logical operator --> And, or, not --> When we use more than one condition
# To make program: Largest/smallest Number, Leap year, Vowel/Consonant, Capital/Small
num1 = 9
num2 = 18
num3 = 87
if num1 > num2 and num1 > num3:
    print("num1 is", num1, "and greater than num2 and num3")
elif num2 > num1 and num2 > num3:
    print("num2 is", num2, "and greater than num1 and num3")
else:
    print("num3 is", num3, "and greater than num1 and num2")

# Vowel
myAlphabet = input("Enter any alphabet: ")
if myAlphabet == 'a' or myAlphabet == 'e' or myAlphabet == 'i' or myAlphabet == 'o' or myAlphabet == 'u':
    print(myAlphabet, "is a Vowel")
else:
    print(myAlphabet, "is a Consonant")

# Letter grade
marks = int(input("Please Enter your marks here: "))
if 80 <= marks <= 100:
    print("A+")
elif 70 <= marks <= 79:
    print("A")
elif marks >= 60 and marks <= 69:  # 2 different way to write
    print("-A")
elif marks >= 50 and marks <= 59:
    print("B+")
elif marks >= 40 and marks <= 49:
    print("B")
else:
    print("F")

marks = 20
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("-A")
elif marks >= 50:
    print("B+")
elif marks >= 40:
    print("B")
else:
    print("F")

# You can drive or not in USA?
print("Tell me what is your age? ")
age = int(input())
if age < 18:
    print("You can't drive here in USA")
elif 18 <= age <= 21:
    print("You can go for a learner's license and can drive with an assistance")
elif age > 21:
    print("You can legally drive in USA independently")
