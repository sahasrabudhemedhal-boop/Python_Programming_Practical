#Q14 Write a Python program to accept a person's annual income and calculate the tax payable according to different income slabs.
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax Payable =", tax)
