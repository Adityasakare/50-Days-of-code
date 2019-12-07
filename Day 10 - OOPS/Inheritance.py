class Samsung:
    def __init__(self):
        print(" I am Samsung")

    def makeScreen(self):
        print("I make Screens")

    def Screentest(self):
        print("Screen Test 1 : OK")
        print("Screen Test 2 : OK")
        print("Screen Test 3 : OK")

class Iphone(Samsung):
    def __init__(self):
        print(" I am Apple")

    def A3chips(self):
        print("I make A3 Bionic Chips")
        super().Screentest()

    # def Screentest(self):
    #     print("Screen Test : OK")
   

user = Iphone()
user.A3chips()
user.Screentest()

    