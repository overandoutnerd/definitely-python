patient_id = input("Patient ID: ")
name = input("Patient Name: ")
room = input("Room (General/Private): ")
days = int(input("Days: "))
doctor = float(input("Doctor Charges: ₹"))
diagnostic = float(input("Diagnostic: ₹"))
medicine = float(input("Medicine: ₹"))

if room.lower() == "general":
    room_charge = days * 2000

elif room.lower() == "private":
    room_charge = days*4000

else:
    room_charge = days*2500

total = room_charge + doctor + diagnostic + medicine

if total >= 20000:
    discount = total * .10

elif total >= 10000:
    discount = total * .05

else:
    discount = 0

print("\n========================================")
print(" HOSPITAL & DIAGNOSTIC DASHBOARD")
print("========================================")
print("Patient:", patient_id, name)
print("Room Charges: ₹",room_charge)
print("Total Bill : ₹", round(total,2))
print("Discount : ₹", round(discount,2))
print("Net Amount : ₹", round(total-discount,2))
print("========================================")