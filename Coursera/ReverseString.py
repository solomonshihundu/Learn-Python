message = "AB CDe fGh"

new_string = ""
rev_string = ""

for x in message.lower():
    if x != " ":
        new_string += x
        rev_string = x+rev_string


print(new_string)
print(rev_string)