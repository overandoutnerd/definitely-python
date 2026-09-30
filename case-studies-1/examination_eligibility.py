name = input("Name: ")
attendance = float(input("Attendance: "))
internalMarks = float(input("Internal Marks: "))
assignmentSubmitted = input("Assignment Submitted (Y/N): ")
feePaid = input("Fee Paid (Y/N): ")

assignmentStatus = "Not submitted"
if assignmentSubmitted == "Y":
    assignmentStatus = "Submitted"

feeStatus = "Not paid"
if feePaid == "Y":
    feeStatus = "Paid"

examinationStatus = "Eligible"
if attendance < 75 or internalMarks < 40 or not assignmentSubmitted or not feePaid:
    examinationStatus = "Not eligible"

attendanceBool = "✔️"
if attendance < 75:
    attendanceBool = "❌"

academicBool = "✔️"
if internalMarks < 40:
    academicBool = "❌"

assignmentBool = "✔️"
if assignmentSubmitted != "Y":
    assignmentBool = "❌"

feeBool = "✔️"
if feePaid != "Y":
    feeBool = "❌"

print("-------------------\n")
print("EXAMINATION ELIGIBILITY\n")

print("-------------------\n")
print(f"Student Name: {name}\n")
print("Attendance: {attendance}%\n")
print(f"Internal Marks: {internalMarks}%\n")
print(f"Assignment: {assignmentStatus}\n")
print(f"Fees: {feeStatus}\n")

print("-------------------\n")
print(f"Attendance: {academicBool}\n")
print(f"Academic Criteria: {academicBool}\n")
print(f"Assignment: {assignmentBool}\n")
print(f"Fees: {feeBool}\n")

print("-------------------\n")
print(f"Examination Status: {examinationStatus}\n")
print("-------------------\n")