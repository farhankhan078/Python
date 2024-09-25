a = 0 
b = 1
c = 1

user = int(input("Enter last number in which fibonacci series print: "))
print("Fibonacci series: \n0\n1")

x = 0
while c < user:
    print(c)
    a = b
    b = c
    c = a + b

#counting prime number
    if c > 1:
        flag = 0
        i = 1
        while i <= c:
            if c % i == 0:
                flag += 1
            i += 1
        if flag == 2:
            x += 1
print("Total no. of prime no. is: ",x)
