hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hourful = (hour + (mins + dura ) // 60 )


if (mins + dura) > 60 and hourful > 24:
    while hourful > 24 :
        hourful -= 24
    print("Finalizacion, a las", hourful, ":", (mins + dura) % 60)
elif (mins + dura) > 60 :
    print("Finalizacion, a las", hourful, ":", (mins + dura) % 60)

