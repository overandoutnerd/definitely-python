accountHolder = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
transactionType = input("Enter transaction type (deposit/withdraw/check balance): ").lower()
amount = float(input("Enter transaction amount: "))

withdrawalLimit = 10000
validTypes = ["deposit", "withdraw", "check balance"]

previousBalance = balance

validType = transactionType in validTypes
validAmount = amount > 0
sufficientBalance = balance >= amount
withinLimit = amount <= withdrawalLimit

if transactionType == "withdraw":
    if validAmount and withinLimit and sufficientBalance:
        balance -= amount
        status = "APPROVED"
    else:
        status = "DECLINED"

elif transactionType == "deposit":
    if validAmount:
        balance += amount
        status = "APPROVED"
    else:
        status = "DECLINED"

elif transactionType == "check balance":
    status = "APPROVED"

else:
    status = "DECLINED"

print("\n---------------- ATM DASHBOARD ----------------")
print(f"Account Holder      : {accountHolder}")
print(f"Current Balance     : {previousBalance}")
print(f"Transaction Type    : {transactionType}")
print(f"Transaction Amount  : {amount}")
print("Sufficient Balance  :", "YES" if sufficientBalance else "NO")
print("Within Limit        :", "YES" if withinLimit else "NO")
print("Valid Amount        :", "YES" if validAmount else "NO")
print(f"Transaction Status  : {status}")
print(f"Previous Balance    : {previousBalance}")
print(f"New Balance         : {balance}")