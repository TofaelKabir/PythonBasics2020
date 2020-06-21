# Using the property of other class

# class1:


class IPhone:  # -->Base/Super/Parent class

    def makeACall(self):  # function1
        print("You can make a call")

    def sendMessage(self):  # function2
        print("You can send Message")


# class2 which inherits IPhone class
class Samsung(IPhone):  # -->in() mentioned the class name that is being inherited -->Derived/Sub/child class

    def takeAPhoto(self):  # function3
        print("You can a take a photo")


s1 = Samsung()  # obj creation and call the func
s1.sendMessage()  # this func comes from IPhone class
s1.makeACall()  # this func comes from IPhone class
s1.takeAPhoto()

# Note: Samsung is sub class and Iphone is Super class-->we can check it by using a func
print("------------------------------------------")
print(issubclass(Samsung, IPhone))  # True if Samsung is sub class of Iphone
