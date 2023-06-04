# organisms.py
import random
from src.genetics import Synapse


class Organism:
    def __init__(self, x, y, environment, genes):
        self.x = x
        self.y = y
        self.environment = environment
        self.genes = genes
        self.reproduction_chance = 0.1  # Chance to reproduce at each time step
        self.brain = self.build_brain(genes)

    def move(self):
        # Define possible movements
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])

        # Compute new coordinates
        new_x = self.x + dx
        new_y = self.y + dy

        # Check if the new coordinates are inside the grid
        if (0 <= new_x < self.environment.width) and (
            0 <= new_y < self.environment.height
        ):
            # Check if the new cell is unoccupied
            if self.environment.grid[new_y][new_x] is None:
                # Remove organism from the old cell
                self.environment.grid[self.y][self.x] = None

                # Update organism coordinates
                self.x = new_x
                self.y = new_y

                # Add organism to the new cell
                self.environment.grid[self.y][self.x] = self

    def reproduce(self):
        # Check if the organism will reproduce
        if random.random() < self.reproduction_chance:
            # Get a list of empty adjacent cells
            empty_cells = []
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x = self.x + dx
                new_y = self.y + dy
                if (
                    (0 <= new_x < self.environment.width)
                    and (0 <= new_y < self.environment.height)
                    and self.environment.grid[new_y][new_x] is None
                ):
                    empty_cells.append((new_x, new_y))

            # If there is at least one empty cell, select one randomly and create a new organism there
            if empty_cells:
                new_x, new_y = random.choice(empty_cells)
                child = Organism(
                    new_x, new_y, self.environment, self.genes.copy()
                )  # Assuming genes is a list
                return child

    def build_brain(self, genes):
        brain = {
            "input": genes.input_neurons,
            "intermediary": genes.intermediary_neurons,
            "output": genes.output_neurons,
        }

        for gene in genes.genes:
            synapse = Synapse(
                brain[gene.input_neuron], brain[gene.output_neuron], gene.weight
            )
            brain[gene.input_neuron].synapses.append(synapse)

        return brain
