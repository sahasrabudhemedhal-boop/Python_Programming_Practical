#Q12) Write a Python program to accept marks obtained in Mathematics, Physics, and Chemistry and determine whether a student is eligible for admission based on subject-wise and overall percentage requirements.

maths = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))

total = maths + physics + chemistry
percentage = (total / 300) * 100

if maths >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
