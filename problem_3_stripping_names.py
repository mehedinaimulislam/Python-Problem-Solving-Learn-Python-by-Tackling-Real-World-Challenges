"""
Reference: Python Crash Course by Eric Matthes

Use a variable to represent a person’s name,
and include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, “\t” and “\n”, at least once.

Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions,
lstrip(), rstrip(), and strip().
"""
person_name = "\tjohn\n"

print("Original Result:")
print(person_name)

print("Modified Result:")
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())


