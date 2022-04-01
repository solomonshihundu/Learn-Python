#format()
name = "Solomon"
number = len(name) * 3
msg = "Hello {}, you lucky number is {}"
print(msg.format(name,number))

msg = "Hello {name}, you lucky number is {number}"
print(msg.format(name = name,number = len(name) * 3))

def student_grade(name, grade):
	return "{name} received {grade}% on the exam".format(name = name,grade = grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#format expresions
#The colon marks the start of expression, 
#.2 signifies two decimal places , 
# f means the actions should be performed on a float
price = 7.5
with_tax = price* 1.09
print("Unformated:",price,with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))

#method converts temp to celsius
def to_celsius(x):
    return (x - 32) * 5/9

# : marks the start of expression
# > aligns the output to the right
# >3 align to the right for a total of 3 spaces
# >6.2f align to the right at 6 spaces and two deciaml places
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))