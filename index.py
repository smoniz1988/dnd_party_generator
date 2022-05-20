# Description: Hail traveler, a new adventure awaits. We need a party! So let's randomly create one
# Could technically move all this code to a party creator class, but that's overengineering at this point I think
# import our character generator
from character_generator import CharacterGenerator

# instantiate a new instance of our character generator
character_generator = CharacterGenerator()

dnd_party = []
max_party_size = 3

# generate our party (loop through 0 to party size) and generate a character
# append it to our party
for i in range(max_party_size):
    character = character_generator.generate()
    dnd_party.append(character)

# generation is complete, lets output the results by looping through our dnd_party
for character in dnd_party:
    print(character.name)
    print(str(character.age) + " Years old")
    print("Level " + str(character.level) + " " + character.dnd_class)
    for stat in character.stats:
        print(stat, character.stats[stat])
    print("=================")
