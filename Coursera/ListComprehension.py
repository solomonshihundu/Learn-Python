#Without List Comprehension, too many lines of code
multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

#Fewer lines of code with list comprehension
multiples = [x*7 for x in range (1,11)]
print(multiples)

#more examples
languages = ["Python","Ruby","Perl","GO","Java","C"]
lengths = [len(length) for length in languages]
print(lengths)

#condition included
z = [x for x in range(0,101) if x % 3 == 0]
print(z)

def odd_numbers(n):
	return [x for x in range(1,n+1) if x%2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []