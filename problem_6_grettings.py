"""
Reference: Python Crash Course by Eric Matthes

Start with the list you used in 'problem_5_names.py',
but instead of just printing each person’s name, print a message to them.
The text of each message should be the same,
but each message should be personalized with the person’s name.
"""
names = ["john", "mike", "adam", "smith"]

message = f"Hello {names[0].title()}! How are you?"
print(message)

message = f"Hello {names[1].title()}! How are you?"
print(message)

message = f"Hello {names[2].title()}! How are you?"
print(message)

message = f"Hello {names[3].title()}! How are you?"
print(message)
