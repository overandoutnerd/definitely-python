userName = input("Enter user name: ")
role = input("Enter role (Student/Faculty/Admin): ")
idCardNumber = input("Enter ID card number: ")
restrictedArea = input("Is it a restricted area? (yes/no): ")

authorizedRoles = ["Student", "Faculty", "Admin"]

if userName == "Abdul" and role == "Student" and idCardNumber == "STU1001":
    idValid = True
elif userName == "Arman" and role == "Faculty" and idCardNumber == "FAC2001":
    idValid = True
elif userName == "Aslam" and role == "Admin" and idCardNumber == "ADM3001":
    idValid = True
else:
    idValid = False

if role in authorizedRoles:
    authorizedRole = True
else:
    authorizedRole = False

if restrictedArea == "yes":
    restrictedAreaStatus = True
else:
    restrictedAreaStatus = False

if restrictedAreaStatus:
    if authorizedRole and idValid:
        accessStatus = "GRANTED"

        if role == "Admin":
            accessLevel = "Full Access"
        elif role == "Faculty":
            accessLevel = "Faculty Access"
        else:
            accessLevel = "Student Access"
    else:
        accessStatus = "DENIED"
        accessLevel = "No Access"

else:
    if idValid:
        accessStatus = "GRANTED"
        accessLevel = "General Access"
    else:
        accessStatus = "DENIED"
        accessLevel = "No Access"

if idValid:
    idCardStatus = "VALID"
else:
    idCardStatus = "INVALID"

if authorizedRole:
    authorizedRoleStatus = "YES"
else:
    authorizedRoleStatus = "NO"

if restrictedAreaStatus:
    restrictedAreaDisplay = "YES"
else:
    restrictedAreaDisplay = "NO"

print("\n--------------------------------------------")
print("        SMART ACCESS DASHBOARD")
print("--------------------------------------------")
print("User Name          :", userName)
print("Role               :", role)
print("ID Card            :", idCardStatus)
print("--------------------------------------------")
print("Authorized Role    :", authorizedRoleStatus)
print("ID Card Valid      :", idCardStatus)
print("Restricted Area    :", restrictedAreaDisplay)
print("--------------------------------------------")
print("Access Level       :", accessLevel)
print("ACCESS STATUS      :", accessStatus)
print("--------------------------------------------")