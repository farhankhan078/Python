n = int(input("Enter any number: "))

i = 2
while i<=n-1:
    if n % i == 0:
        break;
    i = i + 1
if i==n:
    print("The number is Prime")
else:
    print("The number is not prime")