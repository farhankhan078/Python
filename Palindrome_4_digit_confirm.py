n = int(input("Enter 4 digit number: "))
temp = n

if (n < 1000 or n > 9999):
    print("Plz enter 4 digit number")

if (n >= 1000 and n <= 9999):
    _4th = n % 10
    n = n // 10
    _3rd = n % 10
    n = n // 10
    _2nd = n % 10
    _1st = n // 10

    rev = _4th * 1000 + _3rd * 100 + _2nd * 10 + _1st * 1
    if (rev == temp):
        print("This is Palindome")
    if (rev != temp):
        print("This is not Palindrome")