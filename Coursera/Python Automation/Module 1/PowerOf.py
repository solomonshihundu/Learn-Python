def is_power_of(number,base):

    #base case
    if number < base:
        # if the base case has been reached, its a power i.e base**0 = 1
        return number == 1

    #we divide, 8/2 = 4, 4/2 = 2, 2/2 = 1 : it reaches the base case with number == 1 thus tue
    # try 70/10 = 7, 7 / 10 = 0.7 : reaches the base case with number == 0.7 thus false
    return is_power_of(number/base,base)

print(is_power_of(8,2)) #True
print(is_power_of(70,10)) #False
