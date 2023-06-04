# organisms.py
import random


class Organism:
    def __init__(self, x, y, environment, genes):
        self.x = x
        self.y = y
        self.environment = environment
        self.genes = genes

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
        # Define how your organism reproduces here
        pass
