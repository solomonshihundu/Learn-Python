def guest_list(guests):
	for name,age,profession in guests:
		print("{name} is {age} years old and works as {profession}".format(name = name,age = age,profession = profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""