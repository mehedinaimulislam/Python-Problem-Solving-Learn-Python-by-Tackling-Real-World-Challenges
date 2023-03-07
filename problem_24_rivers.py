"""
Reference: Python Crash Course by Eric Matthes

=> Make a dictionary containing three major rivers and the country each river runs through.
    One key-value pair might be 'nile': 'egypt'.

=> Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
=> Use a loop to print the name of each river included in the dictionary.
=> Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    "padma river": "bangladesh",
    "nile river": "egypt",
    "yellow river": "china",
}

for key, value in rivers.items():
    print(f"{key.title()} through {value.title()}.")

print("\nThe following rivers are;")
for river in rivers.keys():
    print(f"\t -{river.title()}")

print(f"\nThe following countries are;")
for country in rivers.values():
    print(f"\t-{country.title()}")
