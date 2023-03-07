"""
Reference: Python Crash Course by Eric Matthes

=> Make a list of five or more usernnames, including the name 'admin'.

Imagine you are writing code that will print a greeting to each user after they log
in to a website.
=> Loop through the list, and print a greeting to each user:

=> If the username is 'admin', print a special greeting,
    such as Hello admin, would you like to see a status report?
=> Otherwise, print a generic greeting, such as Hello Eric, thank you for loggin in again.
"""
user_names = ["@john", "d@smith", "admin", "adele", "mike_24"]

for user_name in user_names:
    if user_name == "admin":
        print(f"Hello {user_name}, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for loggin in again.")