import statistics as stats
import random


class Die:
    def __init__(self, sides=6):
        if type(sides) != int or sides < 1:
            raise Exception('sides must be a positive integer.')
        self._sides = sides
        self._rolls = []

    @property
    def rolls(self):
        return self._rolls

    def roll(self):
        roll = random.randint(1, self._sides)
        self._rolls.append(roll)
        return roll


class Simulation:
    def __init__(self, fnct_to_run, iterations):
        self._fnct_to_run = fnct_to_run
        self._iterations = iterations
        self._results = []
        self.run()

    def run(self):
        for i in range(self._iterations):
            result = self._fnct_to_run()
            self._results.append(result)

    @property
    def mean(self):
        return stats.mean(self._results)

    @property
    def median(self):
        return stats.median(self._results)

    @property
    def mode(self):
        try:
            return stats.mode(self._results)
        except:
            return None


if __name__ == "__main__":
    die = Die()
    sim = Simulation(die.roll, 1000)
    print(sim.mean)
    print(sim.median)
    print(sim.mode)