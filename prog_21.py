#Q22 Write a Python program to accept an integer and determine whether it is a prime number using a `for` loop.

num = int(input("Enter an integer: "))

if num < 2:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
