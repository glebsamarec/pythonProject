income = float(input("Enter the annual income: "))

if income <= 85528:
    tax = round(income * 0.18 - 556.02)
else:
    tax = round(14839.02 + 0.32 * (income - 85528))

if tax < 0:
    tax = 0
print(f"The tax is: {tax:.1f} tallers")