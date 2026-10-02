#Q6.Write a Python program to accept a student's percentage and display the appropriate grade using `if-elif-else` statements. Also validate that the percentage is between 0 and 100.

percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage")

elif percentage >= 90:
    print("Grade A")

elif percentage >= 75:
    print("Grade B")

elif percentage >= 60:
    print("Grade C")

elif percentage >= 50:
    print("Grade D")

else:
    print("Grade F")

