message = "So they gant change" #string with erronous content
print(message)

new_message = message[:8] + "c" + message[9:] #modified string by accessing the desired character index
print(new_message) 

print("change" in message)
print("coming" in message)