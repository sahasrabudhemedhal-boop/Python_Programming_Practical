#Write a Python program to accept the number of electricity units consumed by a consumer and calculate the electricity bill according to different consumption slabs.

units=int(input("Enter units consumed:"))

if units<100:
  bill=units*5

elif units<200:
  bill=units*7

else:
  bill=units*10
print("Electricity bill is:",bill)
