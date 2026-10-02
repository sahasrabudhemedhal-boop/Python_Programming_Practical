#Q4) Write a Python program to accept a time duration in seconds and convert it into hours, minutes, and seconds.
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

