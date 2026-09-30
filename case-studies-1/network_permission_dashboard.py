userName = input("Enter user name: ")
userRole = input("Enter user role: ")

READ = 1
WRITE = 2
EXECUTE = 4

permission = READ | WRITE

if permission & READ:
    readStatus = "ALLOWED"
else:
    readStatus = "DENIED"

if permission & WRITE:
    writeStatus = "ALLOWED"
else:
    writeStatus = "DENIED"

if permission & EXECUTE:
    executeStatus = "ALLOWED"
else:
    executeStatus = "DENIED"

print("\n------ NETWORK PERMISSION DASHBOARD ------")
print(f"User Name        : {userName}", )
print(f"User Role        : {userRole}", )
print("------------------------------------------")
print(f"READ             : 001 : {readStatus}", )
print(f"WRITE            : 010 : {writeStatus}", )
print(f"EXECUTE          : 100 : {executeStatus}", )
print("------------------------------------------")
print(f"Permission Value : {permission}", )
print("Binary Value     : 011")