#Q2)Write a Python program to accept an employee's basic salary and calculate DA, HRA, gross salary, tax deduction, and net salary.

# Accept basic salary
basic = float(input("Enter basic salary: "))

# Calculate DA and HRA
DA = 0.10 * basic
HRA = 0.20 * basic

# Calculate gross salary
gross = basic + DA + HRA

# Calculate tax deduction
tax = 0.05 * gross

# Calculate net salary
net = gross - tax

# Display the result
print("DA =", DA)
print("HRA =", HRA)
print("Gross Salary =", gross)
print("Tax Deduction =", tax)
print("Net Salary =", net)
