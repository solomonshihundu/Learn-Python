#Using the .sort() method, changes the exisiting list to a sorted list
numbers = [6,1,9,2,8,0]
print(numbers)
numbers.sort()
print(numbers)

#Using the sorted(list), creates a new list containing sorted elements
names = ["Solo","Kim","Albert","Naom"]
print(names)
new_names = sorted(names)
print (new_names)
print (names)

#Using a key to sort
print(sorted(names,key = len))

