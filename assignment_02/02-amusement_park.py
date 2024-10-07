# This lesson emphasizes the importance of testing if-else statements.

age = int(input(f"Enter your age: "))

# Note: The 'age >= 100' must be before 'age > 60' because order matters.
if age < 4 or age >= 100:
    print("Admission is free!")
elif age < 18: 
    print("Admission is $25.")
elif age > 60:
    print("Admission is $35.")
# elif age >= 100:
#   print("Admission is free!")
else: 
    print("Admission is $40.")
