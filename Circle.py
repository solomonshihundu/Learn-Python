class Circle:
    def __init__(self,radius):
        self.radius = radius

    def circumference(self):
        pi = 3.142
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue

    def printCircumference(self):
        myCircumference = self.circumference()    
        print("Circumference of "+ str(self.radius)+ " = " + str(myCircumference))

radius1 = 12
radius2 = 7
radius3 = 14

circle1 = Circle(radius1)
circle1.printCircumference()

circle2 = Circle(radius2)
circle2.printCircumference()

circle3 = Circle(radius3)
circle3.printCircumference()





