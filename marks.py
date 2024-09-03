
student_name = input("Enter the student's name: ")

math_marks = int(input("Enter marks for Math (out of 100): "))
science_marks = int(input("Enter marks for Science (out of 100): "))
english_marks = int(input("Enter marks for English (out of 100): "))
history_marks = int(input("Enter marks for History (out of 100): "))
SST_marks = int(input("Enter marks for SST (out of 100): "))

total_marks = math_marks + science_marks + english_marks + history_marks + SST_marks

max_marks = 5 * 100  
percentage = (total_marks / max_marks) * 100

# Determine the grade based on the percentage
if percentage >= 60:
    grade = '1st Div'
elif percentage >= 45:
    grade = '2nd Div'
elif percentage >= 33:
    grade = '3rd Div'
else:
    grade = 'Fail'


print("\nMarksheet of:", student_name)
print("-" * 30)
print("Subject:\tMaximum Marks\t Obtained Marks\tResult"
print(f"Math: {math_marks}/100\t ")
print(f"Science: {science_marks}/100")
print(f"English: {english_marks}/100")
print(f"History: {history_marks}/100")
print(f"SST: {SST_marks}/100")
print("-" * 30)
print(f"Total Marks: {total_marks}/{max_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
