import ipaddress


print("Hellow World")
print(type(6))
print(type(55.5))
x=3
y=5
z=x+y
print(z)

str1 = "I am legend"
str2 = "Not so much though"
str3 = "But at the very end"
print(str1,str2,str3)#inserts spaces in between strings
print(str1+str2+str3)#doesn't include spaces in between words
print(str(8)+str(9))#concatnates two strings 
print(8+9)#performs arithmetic operation
x=4
#print("Is this a string of "+x) ## will result in type error
#string formating
num=22/7
print(f"The value of num is {num}")
pi = "{:.2f}".format(num)#formats the output to 2 decimal places
pi = "{:.4f}".format(num)#formats the output to 4 decimal places
print(pi)

#List and Dictionaries
hostnames=["R1","R2","R3","R4"]#This is a list Declaration(Ordered)
print(type(hostnames))
print(len(hostnames))
print(hostnames)
print(hostnames[-2])
print(hostnames[1])

ipAddress={"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}#This is a dictionary declaration
#Its is unordered and relies on key value pairs
print(type(ipAddress))
print(ipAddress)
print(ipAddress['R1'])
ipAddress["S1"]="10.1.1.10"#Adding data into existing dictonary
print(ipAddress)
ipAddress["3"]=["10.3.3.1","10.3.3.2","10.3.3.3"] #List inside dictionary
print(ipAddress)

####Input Function
firstName = input("Please enter your name here  ")
print("Hello "+firstName)