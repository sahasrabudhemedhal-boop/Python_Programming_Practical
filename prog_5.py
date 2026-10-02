# Q5)Write a Python program to accept the price and quantity of three products and calculate the subtotal, discount, GST, and final payable amount.

p1=float(input("Enter price of product 1:"))
p2=float(input("Enter price of product 2:"))
p3=float(input("Enter price of product 3:"))

q1=int(input("Enter quantity of product 1:"))
q2=int(input("Enter quantity of product 2:"))
q3=int(input("Enter quantity of product 3:"))

s1=p1*q1+p2*q2+p3*q3
print("Sobtotal:",s1)

discount=0.05*s1
amount=s1-discount
print("Discounted price is:",amount)

gst=0.18*amount
print("GST amount is:",gst)

final_amount=amount+gst
print("Total amount is:",final_amount)
