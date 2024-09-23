end = int(input("Enter last no.: "))
start = 1
while start <= end:
    c = 1
    while start <= end and c <= 10:
        print(start)
        start += 1
        c += 1
    
    if start > end:
        print("All numbers have been printed.")
        break

    ch = input("Do you want to continue with the next 10 numbers? [Y/N]: ")
    if ch != 'y' and ch != 'Y':
        print("Ok, not printing other 10 digit")
        break

