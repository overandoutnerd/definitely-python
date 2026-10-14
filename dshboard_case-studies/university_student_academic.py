sid = input("Student ID: ")
name = input("Name: ")
dept = input("Department: ")
marks = []

for subject in ["Python","DBMS","Mathematics","OS","Networks"]:
    marks.append(float(input(subject + " marks: ")))

total = sum(marks)
average = total / 5
percentage = total / 500 * 100

print("\n========================================")
print(" UNIVERSITY STUDENT DASHBOARD")
print("========================================")
print("Student ID :", sid)
print("Name :", name)
print("Department :", dept)
print("Total :", total)
print("Average :", round(average,2))
print("Percentage :", round(percentage,2),"%")
print("========================================")