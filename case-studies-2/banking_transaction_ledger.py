account = {
    "accountNumber": "516346",
    "holderName": "Abdul Lateef",
    "pin": "3598",
    "balance": 13000.00,
    "transactions": []
}

attempts = 0
authenticated = False

while attempts < 3:
    enteredPin = input("Enter PIN: ")

    if enteredPin == account["pin"]:
        authenticated = True
        break
    else:
        attempts += 1
        print("Incorrect PIN.")

if authenticated:
    print("\nPIN verified successfully.")

    choice = input("Enter transaction type (deposit/withdraw/check balance): ").lower().strip()

    if choice == "deposit":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            account["balance"] += amount
            account["transactions"].append(("Deposit", amount))
            transactionStatus = "APPROVED"
        else:
            transactionStatus = "DECLINED"

    elif choice == "withdraw":
        amount = float(input("Enter withdrawal amount: "))

        validAmount = amount > 0
        sufficientBalance = account["balance"] >= amount

        if validAmount and sufficientBalance:
            account["balance"] -= amount
            account["transactions"].append(("Withdrawal", amount))
            transactionStatus = "APPROVED"
        else:
            transactionStatus = "DECLINED"

    elif choice == "check balance":
        transactionStatus = "APPROVED"

    else:
        transactionStatus = "DECLINED"


else:
    transactionStatus = "DECLINED"
    print("Account locked. Maximum PIN attempts exceeded.")


if authenticated:
    print("\n====================================================")
    print("             BANK STATEMENT REPORT")
    print("====================================================")
    print(f"Account Number : {account['accountNumber']}")
    print(f"Holder Name    : {account['holderName']}")
    print("--------------------------------------------------")
    print("Type             | Amount ($)   | Balance ($)")
    print("--------------------------------------------------")

    runningBalance = 13000.00

    print(f"Initial Balance  | ---          | {runningBalance:>.2f}")

    for transaction in account["transactions"]:
        transactionType, amount = transaction

        if transactionType == "Deposit":
            runningBalance += amount
        else:
            runningBalance -= amount

        print(f"{transactionType:<16} | {amount:.2f}     | {runningBalance:>.2f}")

    print("--------------------------------------------------")
    print(f"Closing Balance  : ${account['balance']}")
    print(f"Transaction Status: {transactionStatus}")
    print("====================================================")