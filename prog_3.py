#Write a Python program to accept the number of electricity units consumed by a consumer and calculate the electricity bill according to different consumption slabs.

# Accept time duration in seconds
total_seconds = int(input("Enter time duration in seconds: "))

# Calculate hours
hours = total_seconds // 3600

# Calculate remaining seconds
remaining_seconds = total_seconds % 3600

# Calculate minutes
minutes = remaining_seconds // 60

# Calculate remaining seconds
seconds = remaining_seconds % 60

# Display the result
print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)
```
