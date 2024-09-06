name = input("Enter the student's name: ")

math_marks = int(input("Enter marks for Math (out of 100): "))
science_marks = int(input("Enter marks for Science (out of 100): "))
english_marks = int(input("Enter marks for English (out of 100): "))
history_marks = int(input("Enter marks for History (out of 100): "))
SST_marks = int(input("Enter marks for SST (out of 100): "))

total_marks = math_marks + science_marks + english_marks + history_marks + SST_marks
max_marks = 5 * 100 
percentage = (total_marks / max_marks) * 100

math_grade = 'P' if math_marks >= 34 else 'F'
science_grade = 'P' if science_marks >= 34 else 'F'
english_grade = 'P' if english_marks >= 34 else 'F'
history_grade = 'P' if history_marks >= 34 else 'F'
SST_grade = 'P' if SST_marks >= 34 else 'F'

if percentage >= 60:
    result = '1st Division'
elif percentage >= 50:
    result = '2nd Division'
elif percentage >= 33:
    result = '3rd Division'
else:
    result = 'Fail'

print("\nName:", name)
print("-" * 30)
print("Subject\t\tMax_Marks\tObtained_Marks\tGrade\n")
print(f"Math\t\t100\t\t{math_marks}\t\t{math_grade}")
print(f"Science\t\t100\t\t{science_marks}\t\t{science_grade}")
print(f"English\t\t100\t\t{english_marks}\t\t{english_grade}")
print(f"History\t\t100\t\t{history_marks}\t\t{history_grade}")
print(f"SST\t\t100\t\t{SST_marks}\t\t{SST_grade}")

print("-" * 30)
print(f"Total Marks: {total_marks}\tPercentage: {percentage:.2f}%\tOverall Result: {result}")
