#Prints multiples of given number, between range 0 - 100
def multiples(number):
    for i in range (100):
        if i % number == 0:
            print(i)

multiples(7)