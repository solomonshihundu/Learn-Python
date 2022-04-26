#Function checks whether input lenght is greater than two chars
# Returns Boolen
def is_valid(user):
    if(len(user) >= 3):
        return True
    else:
        return False

#function defination, takes iterable as parameter
def validate_user(users):
    for user in users:
        if is_valid(user):
            print(user , "is valid")
        else:
            print(user, "is invalid")

validate_user(["Au","Solomon","Mitchell","Jameson","Pk"])

