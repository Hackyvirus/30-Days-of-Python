# 10. Calculate simple interest

P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time Period: "))

print("\nCalculating Simple Interest -----\n")
I = (P * R * T)/100

print(f"Simple Interest: {I}")