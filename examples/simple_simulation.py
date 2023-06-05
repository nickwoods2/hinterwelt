# examples/simple_simulation.py
import sys
import numpy as np
import os

sys.path.append("..")  # add the parent directory to the Python path

# examples/simple_simulation.py
from src.organisms import Organism
from src.environment import Environment
from src.simulation import Simulation


def run_simple_simulation():
    # Create a 10x10 environment
    environment = Environment(20, 20)

    # Set up a genome that biases the organism to move up
    genome_up = [
        0
    ] * 244  # 234 is the total size of the genome, 0 is arbitrary initialization
    genome_up[-4] = 1.0  # Bias towards "move up" action in the output layer
    genome1 = genome_up

    genome2 = list(np.random.uniform(low=-1.0, high=1.0, size=(244,)))
    genome3 = list(np.random.uniform(low=-1.0, high=1.0, size=(244,)))

    organism1 = Organism(1, 1, environment, genome1)
    organism2 = Organism(3, 7, environment, genome2)
    organism3 = Organism(9, 5, environment, genome3)

    # Create a simulation
    simulation = Simulation(environment, [organism1, organism2, organism3])

    # Plot the initial state of the environment
    # environment.plot(0)

    # Run the simulation for 20 time steps
    simulation.run(20)


run_simple_simulation()
