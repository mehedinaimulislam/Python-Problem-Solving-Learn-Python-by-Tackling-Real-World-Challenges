"""
Reference: Python Crash Course by Eric Matthes

=> Use a list comprehension to generate a list of the first 10 cubes.
"""
# for number in range(1, 11):
#     print(number ** 3)

list_comprehension = [cube ** 3 for cube in range(1, 11)]
print(list_comprehension)