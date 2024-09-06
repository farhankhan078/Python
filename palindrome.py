num = int(input("Enter 3 digit no.: "))

if (num // 100 == num % 10):
    print("palindrome")
if (num // 100 != num % 10):
    print("not palindrome")