subtotal = 0
items = 0
while True:
    product = input("Product (done to finish): ")
    if product.lower() == "done":
        break
    quantity = int(input("Quantity: "))
    if quantity <= 0:
        print("Invalid quantity")
        continue
    price = float(input("Price: ₹"))
    subtotal += quantity * price
    items += quantity

if subtotal >= 5000:
    discount = subtotal * .10
elif subtotal >= 2500:
    discount = subtotal * .05
else: discount = 0

print("\n========================================")
print(" SUPERMARKET & SHOPPING MALL")
print(" SALES DASHBOARD")
print("========================================")
print("Items:", items)
print("Subtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Final: ₹", subtotal-discount)
print("========================================")