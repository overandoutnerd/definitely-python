studentName = input("Enter student name: ")
studentId = input("Enter student ID: ")
category = input("Enter category (UG/PG/Staff): ")

foodItem = input("Choose item (Burger/Pizza/Sandwich): ")
quantity = int(input("Enter quantity: "))
coupon = input("Enter coupon code (SAVE10 or NO): ")
delivery = input("Delivery required? (yes/no): ")
balance = float(input("Enter available balance: ₹"))

menu = ["Burger", "Pizza", "Sandwich"]

itemAvailable = foodItem in menu

if foodItem == "Burger":
    price = 80
elif foodItem == "Pizza":
    price = 150
elif foodItem == "Sandwich":
    price = 60
else:
    price = 0

subtotal = price * quantity

if category == "UG" or category == "PG":
    studentDiscount = subtotal * 10 / 100
else:
    studentDiscount = 0

if coupon == "SAVE10":
    couponValid = True
    couponDiscount = subtotal * 10 / 100
else:
    couponValid = False
    couponDiscount = 0

if delivery == "yes":
    deliveryCharge = 30
else:
    deliveryCharge = 0

finalAmount = subtotal - studentDiscount - couponDiscount + deliveryCharge

sufficientBalance = balance >= finalAmount

if itemAvailable and quantity > 0 and sufficientBalance:
    orderStatus = "ORDER CONFIRMED"
    balance -= finalAmount
else:
    orderStatus = "ORDER REJECTED"

itemStatus = "AVAILABLE" if itemAvailable else "UNAVAILABLE"
couponStatus = "VALID" if couponValid else "INVALID"
balanceStatus = "SUFFICIENT" if sufficientBalance else "INSUFFICIENT"

print("\n------ SMART UNIVERSITY CAFETERIA ------")
print(f"STUDENT: {studentName}, ID: {studentId}, Category: {category}")
print(f"Food Item: {foodItem}, Quantity: {quantity}, Price: {price}")
print("----------------------------------------")
print(f"Subtotal         : {subtotal}")
print(f"Student Discount : {studentDiscount}")
print(f"Coupon Discount  : {couponDiscount}")
print(f"Delivery Charge  : {deliveryCharge}")
print(f"FINAL AMOUNT     : {finalAmount}")
print("----------------------------------------")
print(f"Menu Item        : {itemStatus}")
print(f"Coupon           : {couponStatus}")
print(f"Balance          : {balanceStatus}")
print("----------------------------------------")
print(orderStatus)
print(f"Remaining Balance: ₹", balance)