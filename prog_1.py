#Q1) Write a Python program to accept the marks obtained by a student in five subjects and calculate the total marks, average marks, and percentage.

# Accept marks of five subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

# Calculate total marks
total = m1 + m2 + m3 + m4 + m5

# Calculate average marks
average = total / 5

# Calculate percentage
percentage = (total / 500) * 100

# Display the result
print("Total marks =", total)
print("Average marks =", average)
print("Percentage =", percentage, "%")

