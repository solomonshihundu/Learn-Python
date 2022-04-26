#Prints factorial of a number by recusion
def factorial(n):

    if n < 2: #Base case
        return 1

    result = n * factorial(n - 1)
    return result


print(factorial(999))