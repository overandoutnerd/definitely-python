from string import whitespace

registrations = [
    "taylorswift@gmail.com",
    "gracieabrams@gmail.com",
    "abdul@gmail.com",
    "arman@gmail.com",
    "adib@gmail.com",
    "hamza@gmail.com",
    "reyaz@gmail.com",
    "shah@gmail.com",
    "aslM@gmail.com",
    "maqsood@gmail.com"
]

vipList = {
    "abdul@gmail.com",
    "taylorswift@gmail.com",
    "gracieabrams@gmail.com"
}

checkIns = {
    "abdul@gmail.com",
    "arman@gmail.com",
    "aslam@gmail.com",
    "taylorswift@gmail.com"
}

uniqueRegistrants = set(registrations)

vipGuestsPresent = uniqueRegistrants.intersection(vipList)
vipGuestsPresent = vipGuestsPresent.intersection(checkIns)

absentees = uniqueRegistrants.difference(checkIns)

totalUniqueRegistrations = len(uniqueRegistrants)
actualCheckIns = len(uniqueRegistrants.intersection(checkIns))
totalAbsentees = len(absentees)
totalVipGuestsPresent = len(vipGuestsPresent)

if totalUniqueRegistrations > 0:
    attendanceRate = (actualCheckIns / totalUniqueRegistrations) * 100
else:
    attendanceRate = 0


email = input("Enter your email: ").lower().strip()

isRegistered = email in uniqueRegistrants
isCheckedIn = email in checkIns
isVip = email in vipList

if isRegistered and isCheckedIn:
    entryStatus = "CHECKED IN"

    if isVip:
        entryStatus = "VIP CHECKED IN"
    else:
        entryStatus = "CHECKED IN"

elif isRegistered and not isCheckedIn:
    entryStatus = "REGISTERED BUT ABSENT"

else:
    entryStatus = "NOT REGISTERED"


print("====================================================")
print("        EVENT CHECK-IN ANALYTICS DASHBOARD")
print("====================================================")
print("Metric                       | Count")
print("--------------------------------------------------")
print(f"Total Unique Registrations  | {totalUniqueRegistrations}")
print(f"Actual Check-ins            | {actualCheckIns}")
print(f"Absentees                   | {totalAbsentees}")
print(f"VIP Guests Present          | {totalVipGuestsPresent}")
print("--------------------------------------------------")
print(f"Attendance Rate             : {attendanceRate:.2f}%")
print("--------------------------------------------------")