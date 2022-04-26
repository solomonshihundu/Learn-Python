import turtle
from unicodedata import category


class Animal:
    name = ""
    category = ""

    def __init__(self,name):
        self.name = name

    def set_category(self,category):
        self.category = category


class Turtle(Animal):
    category = "reptile"


class Snake(Animal):
    category = "reptile"


print(Turtle.category)
print(Snake.category)

class Zoo:

    def __init__(self) -> None:
        self.current_animals = {}

    def add_animal(self,animal):
        self.current_animals[animal.name] = animal.category

    def totl_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal == category:
                result += 1
        return result

zoo = Zoo()
turtle = Turtle("Turtile")
snake = Snake("Snake")

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.totl_of_category("reptile"))