class Animal:
    sound = ''

    def __init__(self,name) -> None:
        self.name = name

    def speak(self):
        print("{sound} I'm {name}! {sound}".format(name = self.name,sound = self.sound))

class Piglet(Animal):
    sound = "Oink"

class Cow(Animal):
    sound = "Mooo"

hamlet = Piglet("Hamlet")
hamlet.speak()

milky = Cow("Milky")
milky.speak()
