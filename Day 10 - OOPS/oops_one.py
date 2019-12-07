class Phone:                            #Defind Class
    phone_version = "S10"               #Objects
    brand_name = "samsung"
    user_name = ""

    #Constructor

    def __init__(self, user):
        self.user_name = user
        

    def Boot_logo(self):                        #Methods 
        print("SAMSUNG" , self.phone_version)

#  aditya = Phone("Aditya phone")