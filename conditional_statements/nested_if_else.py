ac  = "on"
room_temp = 24

if ac == "on":
    if room_temp < 22:
        print("Room is too cold")
    else:
        print("Temperature is comfortable")
else:
    print("AC is off")

