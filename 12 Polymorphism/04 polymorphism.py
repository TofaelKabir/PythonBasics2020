class Iphone:
    # function1
    def makeACall(self):
        print("I am from Iphone class")

    # function2
    def sendMessage(self):
        print("Message from Iphone class")


class Samsung(Iphone):
    def makeACall(self):
        print("I am from Samsung class")


s1 = Samsung
s1.makeACall(Samsung)  # "I am from Samsung class"--> method is overridden so new message will print
s1.makeACall(Iphone)  # "I am from Samsung class"--> method is overridden so new message will print
s1.sendMessage(Samsung)  # Message from Iphone class-->common method accessable from both class
s1.sendMessage(Iphone)  # Message from Iphone class-->common method accessable from both class