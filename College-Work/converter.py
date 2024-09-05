print("__________Converter__________")
print("Enter 1 to Convert Temperature\n")
print("Enter 2 to Convert Second into Hour, Minute and Second\n")
print("Enter 3 to Convert Kilometer to Meter\n")
choice = int(input("Enter your Choice: "))

#temperature converter
if choice == 1:
    print("Enter 1 to Convert Celsius into Fahrenheit\n")    
    print("Enter 2 to Convert Fahrenheit into Celsius\n")    
    temp_ch = int(input("Enter your Choice: "))
    if temp_ch == 1:
        c = int(input("Enter celsius: "))
        fahrenheit = (c * 9/5) + 32
        print(f"{c}C = {fahrenheit}F")
    elif temp_ch == 2:
        f = int(input("Enter Fahrenheit: "))
        celsius = (f - 32) * 5//9
        print(f"{f}F= {celsius}C")
    else:
        print("Wrong choice")

#second into hr,min and sec
elif choice == 2:
    sec = int(input("Enter second to convert into Hour,Minute and second"))
    hr = sec // 3600
    remains_sec = sec % 3600
    min = remains_sec // 60
    second_left = remains_sec % 60
    print(f"{sec} is {hr}Hour:{min}Minutes:{second_left}Seconds: ")

#kilometer to meter, meter to kilometer
elif choice == 3:
    print("Enter 1 to convert km to m\n")
    print("Enter 2 to convert m to km\n")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        print("Enter kilometer to convert into meter. (km to m): ")
        km = int(input())
        meter = km * 1000
        print(f"{km} Kilometer = {meter} Meter")
    elif ch == 2:
        print("Enter kilometer to convert into meter. (km to m): ")
        m = int(input())
        kilo_meter = m // 1000
        print(f"{m} Meter = {kilo_meter} Kilometer")
    else:
        print("Wrong choice")

else:
    print("Wrong choice. Plz Try Again...")
    
    

