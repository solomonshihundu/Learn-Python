def skip_elements(elements):
	# code goes here
	elements_copy = elements
	new_list = []
	for index,element in enumerate(elements_copy):
		if index % 2 == 0:
			new_list.append(element)

	
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']