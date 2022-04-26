from msilib.schema import MsiFileHash


message = "  This is a simple Message Written for demo Only  "

#coneverts string to upper case
print(message.upper()) #THIS IS A SIMPLE MESSAGE WRITTEN FOR DEMO ONLY 

#converts string to lower case
print(message.lower())#this is a simple message written for demo only 

#removes whitespace,tabs and unnecessary new line chars 
print(message.lstrip())#This is a simple Message Written for demo Only

#removes whitespace,tabs and unnecessary new line chars to the left
print(message.lstrip())

#removes whitespace,tabs and unnecessary new line chars to the right
print(message.rstrip())

#prints number of times t appears in a string
print(message.count("t"))#2

#Returns True if string ends with only
print(message.strip().lower().endswith("only"))# True

#Returns True if string is numeric
print(message.isnumeric())#False

#Returns a string made of values given concatnated with initial string 
print(" ".join(["But","now","its","for","practise"]))#


#Return a list of substring from initial string that 
#were separated with white spaces
print(message.split())#['This', 'is', 'a', 'simple', 'Message', 'Written', 'for', 'demo', 'Only']

