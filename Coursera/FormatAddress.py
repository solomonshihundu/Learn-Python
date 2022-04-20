def format_address(address_string):
  # Declare variables
  house_num = ''
  street_name = ' '
  str_list = []
  # Separate the address string into parts
  address_parts = address_string.split()
  # Traverse through the address parts
  for part in address_parts:
    # Determine if the address part is the
    # house number or part of the street name
    if part.isdigit():
        house_num = part
    else:
        str_list.append(part)
        street_name  = " ".join(str_list)
  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {house_num} on street named {street_name}".format(house_num = house_num,street_name = street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
