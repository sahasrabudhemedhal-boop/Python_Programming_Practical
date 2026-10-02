#Q25 Write a Python program to accept an integer and display all its factors. Also display the total number of factors.
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
        count = count + 1

print("Total Factors =", count)
