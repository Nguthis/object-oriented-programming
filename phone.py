class Smartphone:
    def __init__(self,name,model_year,storage,ram,battery):
        self.name = name
        self.model_year = model_year
        self.storage = storage
        self.ram = ram
        self.battery = battery
    #method to get about phone
    def aboutPhone(self):
        print("About this phone:\nName:"+self.name+"\nModel year:"+self.model_year+"\nStorage:"+str(self.storage)+"\nRam:"+str(self.ram)+"\nBattery:"+str(self.battery))
class Samsung(Smartphone):
    #To know if the phone can play fortnite game
    def play_Fortnite(self):
        print("This phone can play Fortnite")
    pass

class Apple(Smartphone):
    def play_Fortnite(self):
        print("This phone can play Fortnite")
    pass

class Xiaomi(Smartphone):
    def play_Fortnite(self):
        print("This phone cannot play Fortnite")
    pass
