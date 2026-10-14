def item_amount(price,qty):
    return price * qty

def tax(amount,rate = 5):
    return amount * rate / 100

def dashboard(table,subtotal,tax_amount):
    print("\n====================================")
    print(" RESTAURANT ORDER DASHBOARD")
    print("====================================")
    print("Table:", table)
    print("Subtotal: ₹",subtotal)
    print("Tax: ₹", tax_amount)
    print("Total: ₹", subtotal + tax_amount)

menu = {
    "Biryani": 250,
    "Juice": 80,
    "Dessert": 120,
    "Coffee": 60
}

table = input("Table: ")

subtotal = 0

for item,price in menu.items():
    quantity = int(input(item + " quantity: "))
    subtotal += item_amount(price, quantity)

tax_amount = tax(subtotal)

dashboard(table, subtotal, tax_amount)