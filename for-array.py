print("ALL DEVICES")
devices = ["R1","R2","R3","R4","R5","S1","S2","S3","S4"]
for i in devices:
    print(i)

print("ONLY ROUTERS")
for i in devices:
    if "R" in i:
        print(i)

print("ONLY SWITCHES")
switches=[]
for i in devices:
    if "S" in i:
        switches.append(i)
print(switches)        