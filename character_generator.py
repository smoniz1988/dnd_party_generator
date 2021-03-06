import random

from character import Character
from stat_generator import StatGenerator


# create a class to handle generation (classes lend themselves to single responsibility. this class generates
# characters, that's it)
class CharacterGenerator:
    def __init__(self):
        pass

    stat_generator = StatGenerator()

    # setup various arrays for "RNG" (random number generation) for character generation
    names = ['Scott', 'Anoke', 'Nicholas', 'Andy', 'Quinn', 'Carmel', 'Jesse', 'Anthony', 'Michelle', 'Anton', 'Zach',
             'Joseph', 'Dennis']

    titles = ['the Great', 'the Powerful', 'the Weak', 'the Shy', 'the Ferocious', 'the Programmer', 'the Beautiful',
              'the Darkness ', 'the Everlasting Light', 'the Cunning', 'the Gladiator', 'the Sly', 'the Thief',
              'the Zealous', 'the Mysterious']

    classes = ['Wizard', 'Rogue', 'Mage', 'Fighter', 'Warlock', 'Paladin', 'Barbarian', 'Cleric', 'Druid']

    # create a generate function to randomize names, age, class
    def generate(self):
        character = Character()
        character.name = self.names[random.randint(0, len(self.names) - 1)]
        character.name += ", " + self.titles[random.randint(0, len(self.titles) - 1)]
        character.age = random.randint(18, 500)
        character.dnd_class = self.classes[random.randint(0, len(self.classes) - 1)]
        character.stats = self.stat_generator.generate()
        return character
