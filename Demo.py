hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

min_total = mins + dura
end_min = min_total%60

hrs_total = hour + (min_total//60)
end_hrs = hrs_total%24

print("END TIME: "+str(end_hrs)+":"+str(end_min))

input()