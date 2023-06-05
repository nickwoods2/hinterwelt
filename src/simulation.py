# evolution_simulation/simulation.py
import time
from .environment import Environment
from .organisms import Organism


class Simulation:
    def __init__(self, environment: Environment, organisms: list[Organism]):
        """
        Initialize a new Simulation.

        :param environment: an instance of Environment in which the simulation takes place.
        :param organisms: a list of Organisms that start in the simulation.
        """
        self.environment = environment
        for organism in organisms:
            self.environment.add_organism(organism)

    def step(self):
        new_organisms = []
        for row in self.environment.grid:
            for organism in row:
                if organism is not None:
                    organism.chance_of_death()
                    if not organism.alive:
                        self.environment.remove_organism(organism)
                        continue

                    organism.move()
                    child = organism.reproduce()
                    if child:
                        new_organisms.append(child)

        for new_organism in new_organisms:
            self.environment.add_organism(new_organism)

        self.environment.step()

    def run(self, steps: int):
        """
        Run the simulation for a given number of time steps.

        :param steps: the number of time steps to run the simulation for.
        """
        for step in range(steps):
            self.step()
            self.environment.plot(step)  # pass the current time step to plot
            time.sleep(1.0)
