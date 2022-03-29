class Circle:
    
    def _init_(self,radius):
        self.radius = radius

    def circumference(self):
        pi = 3.142
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()    
        print("Circumference of "+ str(self.radius)+ " = " + str(myCircumference))
