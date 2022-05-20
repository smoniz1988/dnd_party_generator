# Description: Hail traveler, a new adventure awaits. We need a party! So let's randomly create one

# import our character generator
from character_generator import CharacterGenerator

# instantiate a new instance of our character generator
character_generator = CharacterGenerator()
# array to store all our characters
dnd_party = []
# maximum party size
party_size = 5

# generate our party (loop through 0 to party size) and generate a character
# append it to our party
for i in range(party_size):
    character = character_generator.Generate()
    dnd_party.append(character)

# generation is complete, lets output the results by looping through our dnd_party
for character in dnd_party:
    print(character.name)
    print(str(character.age) + " Years old")
    print("Level " + str(character.level) + " " + character.dnd_class)
    print("=================")
