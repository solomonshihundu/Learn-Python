class Location:
        
    def __init__(self,name,county):
        self.name = name
        self.country = county

    def printData(self):
        print("Hello, my name is "+self.name+" and I'm from "+self.country)

loc = Location("Solomon","Kenya")
loc.printData()