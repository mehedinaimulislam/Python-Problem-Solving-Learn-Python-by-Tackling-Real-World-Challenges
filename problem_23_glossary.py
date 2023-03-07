"""
Reference: Python Crash Course by Eric Matthes

A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.

=> Think of five programming words you’ve learned.
=> Use these words as the keys in your glossary, and store their meanings as values.
=> Print each word and its meaning as neatly formatted output.
=> You might print the word followed by a colon and then its meaning,
or print the word on one line and then print its meaning indented on a second line.
=> Use the newline character ('\n') to insert a blank line between each word-meaning pair in your output.
"""

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

print(f"\nString: {glossary['string']}")
print(f"\nComment: {glossary['comment']}")
print(f"\nList: {glossary['list']}")
print(f"\nLoop: {glossary['loop']}")
print(f"\nDictionary: {glossary['dictionary']}")
