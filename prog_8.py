#Q8. Write a Python program to accept three sides of a triangle, determine whether they form a valid triangle, and if valid, classify it as Equilateral, Isosceles, or Scalene.

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check whether the triangle is valid
if a + b > c and b + c > a and a + c > b:

    
    if a == b and b == c:
        print("Equilateral Triangle")

    elif a == b or b == c or a == c:
        print("Isosceles Triangle")

    else:
        print("Scalene Triangle")

else:
    print("Invalid Triangle")
