productName = input("Product name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))
coupon = input("Coupon code (if available): ")
confirm = bool(input("Confirm order (0/1): "))

subtotal = price * quantity
subtotalDiscount = 0
if subtotal >= 5000:
    subtotalDiscount = 0.1

couponStatus = "Not valid"
couponDiscount = 0

coupons = ("TAYLORSWIFT26", "OLIVIA2026", "AL26")
if coupon in coupons:
    couponStatus = "Valid"
    couponDiscount = 0.2

discount = subtotalDiscount + couponDiscount

deliveryStatus = "Charged"
deliveryCharge = 50
if subtotal >= 3000:
    deliveryStatus = "Free"
    deliveryCharge = 0

print("-------------------\n")
print("ONLINE SHOPPING DASHBOARD")

print("-------------------\n")
print(f"ProductName: {productName}\n")
print(f"Quantity: {quantity}\n")
print(f"Price (per item): {price}\n")
print(f"Coupon Code: {coupon}\n")

print("-------------------\n")
print(f"Subtotal: {subtotal}\n")
print(f"Subtotal Discount: {subtotalDiscount * 100}%\n")
print(f"Coupon discount: {couponDiscount * 100}%\n")
print("Delivery Charge: {deliveryCharge}\n")

total = subtotal + couponDiscount + deliveryCharge
finalAmount = total - (total * discount)
print(f"Final Amount: {finalAmount}\n")

print("-------------------\n")
print(f"Coupon status: {couponStatus}\n")
print(f"Delivery status: {deliveryStatus}\n")
print(f"Order Status: {confirm}\n")
print("-------------------\n")