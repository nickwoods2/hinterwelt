# examples/simple_simulation.py
import sys

sys.path.append("..")  # add the parent directory to the Python path

# examples/simple_simulation.py
from evolution_simulation.organisms import Organism
from evolution_simulation.environment import Environment
from evolution_simulation.simulation import Simulation


def run_simple_simulation():
    # Create a 10x10 environment
    environment = Environment(10, 10)

    # Create some organisms
    organism1 = Organism(1, 1, environment, [])
    organism2 = Organism(3, 7, environment, [])
    organism3 = Organism(9, 5, environment, [])

    # Create a simulation
    simulation = Simulation(environment, [organism1, organism2, organism3])

    # Plot the initial state of the environment
    environment.plot(0)

    # Run the simulation for 20 time steps
    simulation.run(20)


run_simple_simulation()
