storeInventory = {
    101: {"name": "Laptop", "price": 800.00, "stock": 8},
    102: {"name": "Mouse", "price": 25.00, "stock": 45},
    103: {"name": "Keyboard", "price": 50.00, "stock": 12}
}

stockThreshold = 10

def display_lowStock(inventory, threshold):
    lowStockItems = []

    for productId in inventory:
        stock = inventory[productId]["stock"]

        if stock < threshold:
            lowStockItems.append(productId)

    print("\n---------------- LOW STOCK ITEMS ----------------")
    if len(lowStockItems) > 0:

        for productId in lowStockItems:
            name = inventory[productId]["name"]
            stock = inventory[productId]["stock"]
            print(f"{productId} - {name} - Stock: {stock}")
    else:
        print("No low stock items.")


productId = int(input("Enter product ID: "))
quantity = int(input("Enter purchase quantity: "))

validProduct = productId in storeInventory
validQuantity = quantity > 0

if validProduct:
    availableStock = storeInventory[productId]["stock"]
    sufficientStock = availableStock >= quantity
else:
    availableStock = 0
    sufficientStock = False

if validProduct and validQuantity and sufficientStock:
    storeInventory[productId]["stock"] -= quantity
    purchaseStatus = "APPROVED"
else:
    purchaseStatus = "DECLINED"

totalValue = 0
lowStockCount = 0

for productId in storeInventory:
    price = storeInventory[productId]["price"]
    stock = storeInventory[productId]["stock"]

    totalValue += price * stock

    if stock < stockThreshold:
        lowStockCount += 1

display_lowStock(storeInventory, stockThreshold)

print("\n---------------- E-COMMERCE STOCK REPORT ----------------")
print("ID     | Name         | Price ($) | Stock | Status")
print("----------------------------------------------------------")

for productId in storeInventory:
    name = storeInventory[productId]["name"]
    price = storeInventory[productId]["price"]
    stock = storeInventory[productId]["stock"]

    if stock < stockThreshold:
        status = "LOW STOCK"
    else:
        status = "IN STOCK"

    print(f"{productId:<6} | {name:<12} | {price:<9.2f} | {stock:<5} | {status}")

print("----------------------------------------------------------")
print(f"Purchase Status           : {purchaseStatus}")
print(f"Total Inventory Valuation : ${totalValue:,.2f}")
print(f"Low Stock Items Count     : {lowStockCount}")
print("----------------------------------------------------------")
