#define funtion that takes an iterable
def great_friends(friends):
    for friend in friends:
        print("Hey " + friend)

great_friends(["John","Mitchell","Simon"]) # List is an iterable

great_friends("Solomon") # String is also an iterable

# great_friends(30)
# will produce an error as int is not iterable