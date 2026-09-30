students = {
    "S101": ("Arman", 85, 78, 82),
    "S102": ("Aslam", 92, 95, 88),
    "S103": ("Abdul", 65, 60, 61)
}

studentResults = []

for studentId in students:
    name, math, science, english = students[studentId]

    math = float(math)
    science = float(science)
    english = float(english)

    average = (math + science + english) / 3

    if average >= 90:
        letterGrade = "A"

        if average >= 90:
            status = "PASS"
        else:
            status = "FAIL"

    elif average >= 75:
        letterGrade = "B"

        if average >= 75:
            status = "PASS"
        else:
            status = "FAIL"

    elif average >= 50:
        letterGrade = "C"

        if average >= 50:
            status = "PASS"
        else:
            status = "FAIL"

    else:
        letterGrade = "F"

        if average >= 50:
            status = "PASS"
        else:
            status = "FAIL"

    studentResults.append((studentId, name, average, letterGrade, status))

def sortStudents(student):
    return student[2]

studentResults.sort(key=sortStudents, reverse=True)

classAverage = 0

for student in studentResults:
    classAverage += student[2]

classAverage /= len(studentResults)

topStudent = studentResults[0]


print("\n====================================================")
print("        ACADEMIC PERFORMANCE DASHBOARD")
print("====================================================")
print("Rank | ID    | Name       | Average | Grade | Status")
print("====================================================")

rank = 1

for student in studentResults:
    studentId, name, average, letterGrade, status = student

    print(
        f"{rank}    | " f"{studentId}  | " f"{name}      | " f"{average:.2f}   | " f"{letterGrade}     | " f"{status}"
    )

    rank += 1

print("--------------------------------------------------")
print(f"Class Average Score : {classAverage:.2f}")
print(f"Top Scoring Student : {topStudent[1]} ({topStudent[2]:.2f})")
print("====================================================")