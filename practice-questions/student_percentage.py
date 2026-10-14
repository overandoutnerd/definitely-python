student_name = input("Please enter your name: ")
subject1_marks = int(input("Please enter your Maths marks (0-100): "))
subject2_marks = int(input("Please enter your DSA marks (0-100): "))
subject3_marks = int(input("Please enter your Physics marks (0-100): "))

max_marks = 300
obtained_marks = subject1_marks + subject2_marks + subject3_marks

percentage = obtained_marks / max_marks * 100

print(f"Student name: {student_name}")
print(f"Maths marks: {subject1_marks}/100")
print(f"DSA marks: {subject2_marks}/100")
print(f"Physics marks: {subject3_marks}/100")
print(f"Total Marks: {obtained_marks}/300")
print(f"Percentage: {percentage:.2f}%")