"""
Reference: Python Crash Course by Eric Matthes

Consider an amusement park that charge different rates for different age groups:
=> Admission for anyone under age is free.
=> Admission for anyone anyone between the ages of 4 and 18 is $25.
=> admission for anyone age 18 or older is $40.
"""
age = 60

if age < 4:
    print("Your admission fee is free.")
elif age < 18:
    print("Your admission fee is $25.")
else:
    print("Your admission fee is $40.")
