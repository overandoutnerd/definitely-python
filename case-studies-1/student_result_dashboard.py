name = input("Name: ")
studentId = int(input("ID: "))
internalMarks = int(input("Internal Marks (0-20): "))
assignmentMarks = int(input("Assignment Marks (0-15): "))
midtermMarks = int(input("Mid-term Marks (0-25): "))
endsemMarks = int(input("End-sem Marks (0-50): "))
attendance = float(input("Attendance (in percent): "))

print("-------------------\n")
print("Student Result Dashboard\n")

print("-------------------\n")
print(f"Student Name: {name}\n")
print(f"Student ID: {studentId}\n")

print("-------------------\n")
print(f"Internal Marks: {internalMarks}/20\n")
print(f"Assignment Marks: {assignmentMarks}/15\n")
print(f"Mid-term Marks: {midtermMarks}/25\n")
print(f"End-sem Marks: {endsemMarks}/50\n")

print("-------------------\n")
total= (internalMarks + assignmentMarks + midtermMarks + endsemMarks)
print(f"Total Marks: {total}/110\n")
percentage = (total/110) * 100
print(f"Percentage: {percentage}%\n")
grade = ("")
if 100 >= percentage >= 90:
    grade = "A+"
elif 90 > percentage >= 80:
    grade = "A"
elif 80 < percentage >= 70:
    grade = "B+"
elif 70 < percentage >= 60:
    grade = "B"
elif 60 < percentage >= 40:
    grade = "C"
else:
    grade = "D"
print(f"Grade: {grade}\n")
print(f"Attendance: {attendance}%\n")

print("-------------------\n")
eligibility = "Eligible"
if attendance < 75:
    eligibility = "Not eligible"

print(f"Examination status: {eligibility}\n")

result = "Pass"
if percentage < 33:
    result = "Fail"

print(f"Final Result: {result}\n")
print("-------------------\n")