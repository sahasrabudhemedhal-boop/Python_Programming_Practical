#Q29 Write a Python program to create a menu-driven mathematical application with options to check Prime, Palindrome, Armstrong, Factorial, Fibonacci Series, and Exit. The menu should be displayed repeatedly until the user selects Exit.

while True:
    print("\n1. Prime")
    print("2. Palindrome")
    print("3. Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print("Prime Number")
        else:
            print("Not a Prime Number")

    elif choice == 2:
        num = int(input("Enter a number: "))
        original = num
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if original == reverse:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    elif choice == 3:
        num = int(input("Enter a number: "))
        original = num
        sum = 0

        while num > 0:
            digit = num % 10
            sum = sum + digit ** 3
            num = num // 10

        if sum == original:
            print("Armstrong Number")
        else:
            print("Not an Armstrong Number")

    elif choice == 4:
        num = int(input("Enter a number: "))
        fact = 1

        for i in range(1, num + 1):
            fact = fact * i

        print("Factorial =", fact)

    elif choice == 5:
        n = int(input("Enter number of terms: "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c

        print()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")
