#Q15 Write a Python program to accept monthly mobile data usage in GB and calculate the total bill according to specified usage slabs.

usage = float(input("Enter monthly data usage in GB: "))

if usage <= 5:
    bill = usage * 10
elif usage <= 10:
    bill = usage * 15
else:
    bill = usage * 20

print("Total Bill =", bill)
