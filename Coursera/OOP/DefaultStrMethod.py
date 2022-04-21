class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self) -> str:
        return ("hi, my name is {name}".format(name = self.name))

# Create a new instance with a name of your choice
some_person = Person("Solomon") 
# Call the greeting method
print(some_person)