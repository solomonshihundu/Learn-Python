filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
 
#newfilenames = [x.find(".") for x in filenames if x[index:] == "hpp" x = x[:index] + "." + "hp"]
newfilenames = []
for element in filenames:
    index = element.find(".")
    if element[index+1:] == "hpp":
        new_element = element[:index] + "." + "h"
        newfilenames.append(new_element)
    if element[index+1:] != "hpp":
        newfilenames.append(element)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]