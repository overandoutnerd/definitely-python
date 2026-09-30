waitingList = []

patients = [
    {"name": "Arman", "age": 17, "isEmergency": False},
    {"name": "Aslam", "age": 22, "isEmergency": False},
    {"name": "Rizwan", "age": 24, "isEmergency": True}
]

for patient in patients:
    if patient["isEmergency"]:
        waitingList.insert(0, patient)
    else:
        waitingList.append(patient)


if len(waitingList) > 0:
    nextPatient = waitingList.pop(0)
    print("Doctor is calling:", nextPatient["name"])
else:
    print("No patients waiting.")


waitingList.append(nextPatient)


totalAge = 0

for patient in waitingList:
    age = int(patient["age"])
    totalAge += age

if len(waitingList) > 0:
    averageAge = float(totalAge / len(waitingList))
else:
    averageAge = 0.0


print("====================================================")
print("          CITY HOSPITAL QUEUE DASHBOARD")
print("====================================================")
print("Pos | Patient Name     | Age | Priority Status")
print("----------------------------------------------------")

position = 1

for patient in waitingList:
    name = patient["name"]
    age = patient["age"]

    if patient["isEmergency"]:
        priorityStatus = "CRITICAL"
    else:
        priorityStatus = "REGULAR"

    print(f"{position:<3} | {name:<16} | {age:<3} | {priorityStatus}")
    position += 1

print("----------------------------------------------------")
print(f"Total Waiting Patients : {len(waitingList)}")
print(f"Average Patient Age    : {averageAge:.1f} years")
print("====================================================")