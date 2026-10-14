principal = float(input("Principal amount: "))
rate = float(input("Interest rate: (per year): "))
time = float(input("Time (in years): "))

simple_interest = (principal * rate * time)/100

print(f"Principal amount: ${principal:.2f}")
print(f"Interest rate: {rate:.2f}% per year")
print(f"Time: {time:.2f} years")
print(f"Simple Interest: {simple_interest:.2f}")