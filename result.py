
sub1 = int(input("Enter marks in 1 subject: "))
sub2 = int(input("Enter marks in 2 subject: "))
sub3 = int(input("Enter marks in 3 subject: "))

total_percentage = (100*(sub1 + sub2 + sub3))/300

if(total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print('he is pass',total_percentage)
else:
    print('he is fail',total_percentage)
