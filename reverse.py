n = int(input("Enter any digit number: "))
print("number is : ",n)
rev = 0

while n>0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n//10
print("reverse is ",rev)
