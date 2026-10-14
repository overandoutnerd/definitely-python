principal = float(input("Principal: "))
rate = float(input("Annual interest rate: "))
compounding_frequency = int(input("Annual compounding frequency: "))
time = int(input("Time: (in years): "))

compound_interest = principal * (1 + rate / 100) ** (compounding_frequency * time)

print(f"Principal amount: ${principal:.2f}")
print(f"Interest rate: ${rate:.2f}% per year")
print(f"Compounding frequency: {compounding_frequency:.2f} times per year")
print(f"Time: {time:.2f} years")
print(f"Compound interest: ${compound_interest:.2f}")
