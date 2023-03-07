"""
Reference: Python Crash Course by Eric Matthes

=> Use a dictionary to store people’s favorite numbers.
=> Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in your dictionary.
=> Print each person’s name and their favorite number.
"""

favorite_numbers = {
    "john": 25,
    "mike": 30,
    "smith": 35,
    "adele": 40,
    "jenifer": 45,
}

for key, value in favorite_numbers.items():
    print(f"{key.title()}'s favorite number is {value}.")


