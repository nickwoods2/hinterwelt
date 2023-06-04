# examples/simple_simulation.py
import sys

sys.path.append("..")  # add the parent directory to the Python path

# examples/simple_simulation.py
from src.organisms import Organism
from src.environment import Environment
from src.simulation import Simulation
from src.genetics import Neuron, Gene, Genes


def run_simple_simulation():
    # Create a 10x10 environment
    environment = Environment(10, 10)

    # Define some basic genes for the organisms
    input_neurons = [Neuron() for _ in range(5)]  # example, modify as necessary
    intermediary_neurons = [Neuron() for _ in range(5)]  # example, modify as necessary
    output_neurons = [Neuron() for _ in range(5)]  # example, modify as necessary

    # Let's connect every input neuron to every intermediary neuron, and every
    # intermediary neuron to every output neuron, with weight 0.5 for simplicity
    genes_list = []
    for input_neuron in input_neurons:
        for inter_neuron in intermediary_neurons:
            genes_list.append(Gene(input_neuron, inter_neuron, 0.5))

    for inter_neuron in intermediary_neurons:
        for output_neuron in output_neurons:
            genes_list.append(Gene(inter_neuron, output_neuron, 0.5))

    genes = Genes(input_neurons, intermediary_neurons, output_neurons, genes_list)

    # Create some organisms with these genes
    organism1 = Organism(1, 1, environment, genes)
    organism2 = Organism(3, 7, environment, genes)
    organism3 = Organism(9, 5, environment, genes)

    # Create a simulation
    simulation = Simulation(environment, [organism1, organism2, organism3])

    # Plot the initial state of the environment
    environment.plot(0)

    # Run the simulation for 20 time steps
    simulation.run(20)


run_simple_simulation()
