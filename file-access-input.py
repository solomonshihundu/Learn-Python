devices=[]
file = open("devices.txt","a")#opens the file in append mode
while True:
    device = input("Enter device name: ")
    newItem  = device

    if newItem == 'q' or newItem == 'quit':
        print("All Done !")
        break
    
    file.write(newItem+"\n")
file.close #release memory resources


file = open("devices.txt","r")#opens the file in read mode
for item in file:
    item = item.strip()
    devices.append(item)
    print(item)
file.close()   
print(devices) #release memory resources
