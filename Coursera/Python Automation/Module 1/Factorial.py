#Factorial function defination
def factorial(n):
    result = 1
    for x in range(1,n):
        result = result * x
    return result

#Print factorial of  0 - 9
for n in range(0,10):
    print(n,factorial(n+1))