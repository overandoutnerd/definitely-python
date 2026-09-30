menu = {
    101: ("Samosa", 12.50),
    102: ("French Fries", 5.00),
    103: ("Coffee", 2.50),
    104: ("Pizza", 15.00),
    105: ("Pasta", 10.00)
}

orderList = []
subtotal = 0

while True:
    itemCode = int(input("Enter item code (0 to finish): "))

    if itemCode == 0:
        break

    if itemCode in menu:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            itemName = menu[itemCode][0].title()
            unitPrice = menu[itemCode][1]
            total = unitPrice * quantity

            orderList.append((itemName, quantity, total))
            subtotal += total
        else:
            print("Invalid quantity.")
    else:
        print("Invalid item code.")


tax = subtotal * 0.08

if subtotal > 50:
    discount = 5
else:
    discount = 0

finalAmount = subtotal + tax - discount


print("\n====================================================")
print("              AL SABA RECEIPT")
print("====================================================")
print("Item             | Qty | Unit Price | Total ($)")
print("----------------------------------------------------")

for order in orderList:
    itemName, quantity, total = order

    unitPrice = total / quantity

    print(f"{itemName:<16} | {quantity:<3} | {unitPrice:<10.2f} | {total:.2f}")

print("----------------------------------------------------")
print(f"Subtotal         : ${subtotal:.2f}")
print(f"Tax (8%)         : ${tax:.2f}")
print(f"Discount         : ${discount:.2f}")
print(f"Final Amount     : ${finalAmount:.2f}")
print("====================================================")