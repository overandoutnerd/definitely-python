account = input("Account Number: ")
customer = input("Customer Name: ")
balance = float(input("Opening Balance: ₹"))
print("1.Deposit 2.Withdraw 3.Balance")
choice = input("Choice: ")
if choice == "1":
    amount = float(input("Deposit: ₹"))
    if amount > 0:
        balance += amount
        message = "Deposit Successful"
    else:
        message = "Invalid Amount"
elif choice == "2":
    amount = float(input("Withdrawal: ₹"))
    if amount <= 0:
        message = "Invalid Amount"
    elif amount <= balance:
        balance -= amount
        message = "Withdrawal Successful"
    else:
        message = "Insufficient Balance"
elif choice == "3":
    message = "Balance Enquiry Successful"
else:
    message = "Invalid Choice"

print("\n=================================")
print(" BANKING DASHBOARD")
print("=================================")
print("Account :", account)
print("Customer:", customer)
print("Status :", message)
print("Balance : ₹", round(balance,2))
print("=================================")