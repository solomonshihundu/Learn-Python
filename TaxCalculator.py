income = float(input("Enter the annual income: "))

threshold = 85528

if income <= 0:
    tax = 0.0
elif income < threshold:
    tax = (18/100)*income - 556.2
else:
    tax = 14839.2 + (32/100)*(income - 85528)

if tax < 0:
    tax = 0.0
else:
    tax = round(tax, 0)
print("The tax is:", tax, "thalers")