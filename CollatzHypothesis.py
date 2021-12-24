number = int(input("Enter a number : "))
counter = 0
while number > 0:
    
    if number == 1:
        print(number)
        counter += 1
        break
    
    if number % 2 == 0:#even_number
        number /= 2
        print(number)
        counter += 1
    
    else:#odd_number:
        number *= 3 + 1
        print(number)
        counter += 1
        
else:
     print("Enter a number greater than 0 !")

print("steps = "+str(counter))