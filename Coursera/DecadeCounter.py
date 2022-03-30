def decade_counter(year):
	while year < 50:
		year += 10
	return year

print(decade_counter(4))

for x in range(1, 10, 3): # Consider a span of 3, then x = 1, skips 2,3 x = 4, skips 5,6 x = 7
    print(x)

# Final value of y is 8, outter loop maximum value i.e 9 is the input of the inner loop range
# Thus maximum of inner loop is 8
for x in range(10):
    for y in range(x):
        print(y) #8

    
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

votes(['Yes','No','Maybe'])