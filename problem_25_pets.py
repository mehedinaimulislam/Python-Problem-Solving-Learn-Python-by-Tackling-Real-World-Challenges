"""
References: Python Crash Course by Eric Matthes

=> Make several dictionaries, where the name of each dictionary is the name of a pet.
    => In each dictionary, include the kind of animal and the owner’s name.
=> Store these dictionaries in a list called pets.
=> Next, loop through your list and as you do print everything you know about each pet.
"""
pets = []

pet = {
    "animal": "cat",
    "name": "tom",
    "owner": "mehedi",
}

pets.append(pet)

pet = {
    "animal": "dog",
    "name": "tiger",
    "owner": "john",
}

pets.append(pet)

pet = {
    "animal": "hamster",
    "name": "brown sugar",
    "owner": "mike",
}

pets.append(pet)

for pet in pets:
    print(f"\nDetails about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")

