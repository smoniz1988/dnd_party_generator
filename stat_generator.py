import random

class StatGenerator:
    # stat generation is done using the rolling method
    # we roll a 6sided die 4 times and add the highest 3 numbers together
    # if we rolled 6, 2, 5, 4 that would be 6+5+4=15
    # we do this 6x
    def generate(self):
        stats = {"STR": self.rollStat(), "DEX": self.rollStat(), "CON": self.rollStat(), "WIS": self.rollStat(), "INT": self.rollStat(), "CHA": self.rollStat()}

        return stats

    def rollStat(self):
        results = []

        # roll 4 times and store the results
        for i in range(4):
            results.append(random.randint(1, 6)) #1-6

        # sort the array in descending order (highest to lowest)
        results.sort(reverse=True)

        # sum up values using sum and array slicing (this adds from index 0 to index 3 (exclusive)
        return sum(results[:3])

