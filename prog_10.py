#Q10 Write a Python program to accept an integer and determine whether it is positive, negative, even, odd, or zero.

num = int(input("Enter an integer: "))

if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Zero")

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
