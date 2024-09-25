a = 0
b = 1
c = 1
user = int(input("Enter the last no. to print the fibonacci series (0 to no.): "))

print("Fibonacci Series: \n0\n1")
while c < user:
    print(c)
    a = b
    b = c
    c = a + b