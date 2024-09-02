# Input the student's name
student_name = input("Enter the student's name: ")

# Input marks for each subject individually
math_marks = int(input("Enter marks for Math (out of 100): "))
science_marks = int(input("Enter marks for Science (out of 100): "))
english_marks = int(input("Enter marks for English (out of 100): "))
history_marks = int(input("Enter marks for History (out of 100): "))
SST_marks = int(input("Enter marks for SST (out of 100): "))

# Calculate total marks and percentage
total_marks = math_marks + science_marks + english_marks + history_marks + SST_marks
max_marks = 5 * 100  # Since there are 5 subjects
percentage = (total_marks / max_marks) * 100

# Determine the grade based on the percentage
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B+'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'F'


print("\nMarksheet of:", student_name)
print("-" * 30)
print(f"Math: {math_marks}/100")
print(f"Science: {science_marks}/100")
print(f"English: {english_marks}/100")
print(f"History: {history_marks}/100")
print(f"SST: {SST_marks}/100")
print("-" * 30)
print(f"Total Marks: {total_marks}/{max_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
