print("\n----- define variables in a single line -----")
a, b, c = 10, 20, 30
print("a=", a)  # 10
print("b=", b)  # 20
print("c=", c)  # 30

print("\n----- same value many variables -----")
x = y = "Hello"
print("x=", x)  # Hello
print("y=", y)  # Hello

print("\n----- Use of global and local variable -----")
name1 = "I am outside of function/method --> global variable"
print(name1)


def var():
    name2 = "I am inside of function/method --> local variable"
    print(name2)


var()  # The method is called here to print name 2

print("\n----- Same name for global & local variable -----")
age = 40
print("global variable age:", age)


def varAge():
    age = 50
    print("local variable age:", age)


varAge()

print("\n----- uses of local and global -----")
id1 = 101


def varId():
    id2 = 102
    print("Global id is called from inside the function", id1)
    print("Local id is called from inside the function", id2)


varId()
print("global id is called out side of the function:", id1)
print("local id is called out side of the function:", "sorry first make id2 global, not possible to call")

print("\n----- How to call a global variable from the function 01 -----")
city = "NY"


def varCity():
    global city  # Called as global inside the function
    city = "woodside"
    print("Local variable is called from inside the function: ", city)


varCity()
print("Global variable is called from inside the function if it is declared as global: ", city)

print("\n----- How to call a global variable from the function 02 -----")
phone = 3474005813


def varPhone():
    global phone
    phone = 146488736482
    print("Local variable is called from inside the function: ", phone)


varPhone()
print("Global variable is called from inside the function if it is declared as global: ", phone)
