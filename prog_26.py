#Q26 Write a Python program to accept two positive integers and calculate their GCD and LCM using iterative statements.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    remainder = x % y
    x = y
    y = remainder

gcd = x
lcm = (a * b) // gcd

print("GCD =", gcd)
print("LCM =", lcm)
