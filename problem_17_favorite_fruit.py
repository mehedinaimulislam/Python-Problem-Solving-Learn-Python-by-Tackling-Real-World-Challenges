"""
Reference: Python Crash Course by Eric Matthes

Make a list of your favorite fruits,
and then write a series of independent if statements that check for certain fruits in your list.

=> Make a list of your three favorite fruits and call it favorite_fruits.
=> Write five if statements.
=> Each should check whether a certain kind of fruit is in your list.
    => If the fruit is in your list, the if block should print a statement, such as You really like bananas!
"""

favorite_fruits = ["apple", "pineapple", "mango"]

if "apple" in favorite_fruits:
    print("You really like apples!")
if "strawberrie" in favorite_fruits:
    print("You really like strawberries!")
if "pineapple" in favorite_fruits:
    print("You really like pineapple!")
if "grape" in favorite_fruits:
    print("You really like grape!")
if "mango" in favorite_fruits:
    print("You really like mango!")
