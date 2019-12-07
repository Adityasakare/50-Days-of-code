class Samsung:
    def __init__(self):
        print("I am samsung")

    def makeScreen(self):
        print("I am Screens")

    def test(self):
        print("Screen Test : OK")
       # print("Screen Test : OK")



class Iphone(Samsung):        #if you want to borrow any functions from any other class mentioned parent class name(samsung)
    def __init__(self):
        print("I am Iphone")

    def A3chips(self):
        print("I make A3 Bionics Chips")

    def Itest(self):
        print("A3 chip Test : OK")
        super().test()          #super().function_name used for boroow functions from parent class 


user = Iphone()

user.A3chips()
user.makeScreen()
user.Itest()
user.test()