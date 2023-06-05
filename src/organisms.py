# organisms.py
import random
import math
import numpy as np
from .genetics import Brain


class Organism:
    def __init__(self, x, y, environment, genome):
        self.x = x
        self.y = y
        self.environment = environment
        self.brain = Brain(genome)  # Initialize a new brain for each organism
        self.color = random.randint(0, 255)
        self.genome = genome
        self.reproduction_chance = 0.1
        self.alive = True

    def get_inputs(self):
        """
        Calculate the values of the input neurons based on the current state of the environment.
        """
        inputs = []

        # Compute distances from other organisms and walls, and the color of the nearest organism
        # These methods will need to be implemented:
        inputs.append(self.distance_from_organism_positive_x())
        inputs.append(self.distance_from_organism_negative_x())
        inputs.append(self.distance_from_organism_positive_y())
        inputs.append(self.distance_from_organism_negative_y())
        inputs.append(self.euclidean_distance_to_nearest_organism())
        inputs.append(self.distance_from_wall_x())
        inputs.append(self.distance_from_wall_y())
        inputs.append(self.color_of_nearest_organism())

        return inputs

    def move(self):
        """
        Determine the action to take based on the output of the neural network.
        """
        inputs = self.get_inputs()
        action = self.brain.decide(inputs)

        if action == 0:
            self.move_left()
        elif action == 1:
            self.move_right()
        elif action == 2:
            self.move_up()
        elif action == 3:
            self.move_down()

    def move_up(self):
        if self.y < self.environment.height - 1:
            self.environment.remove_organism(self)
            self.y += 1
            self.environment.add_organism(self)

    def move_down(self):
        if self.y > 0:
            self.environment.remove_organism(self)
            self.y -= 1
            self.environment.add_organism(self)

    def move_right(self):
        if self.x < self.environment.width - 1:
            self.environment.remove_organism(self)
            self.x += 1
            self.environment.add_organism(self)

    def move_left(self):
        if self.x > 0:
            self.environment.remove_organism(self)
            self.x -= 1
            self.environment.add_organism(self)

    def chance_of_death(self):
        # Just an example. You can use any criteria that make sense for your simulation.
        distance_to_nearest_organism = self.euclidean_distance_to_nearest_organism()
        distance_to_point = np.sqrt((self.x - 5) ** 2 + (self.y - 5) ** 2)

        # Calculate probability of death based on criteria
        death_probability = min(distance_to_nearest_organism / 100, 1) * min(
            distance_to_point / 100, 1
        )

        # Increase the chance of death if there are more organisms
        num_organisms = sum(
            [
                1
                for row in self.environment.grid
                for organism in row
                if organism is not None
            ]
        )
        death_probability += 0.01 * num_organisms
        death_probability = 0
        # Determine if organism dies
        if np.random.random() < death_probability:
            self.alive = False

    def reproduce(self):
        # The organism reproduces if a random number is less than its reproduction chance
        if np.random.random() < self.reproduction_chance:
            # Create a new genome by adding a small random number to each gene
            new_genome = []
            for gene in self.genome:
                mutation = np.random.normal(
                    0, 0.01
                )  # a random number from a normal distribution
                new_gene = gene + mutation
                new_genome.append(new_gene)

            # Find the nearest available location in the grid
            directions = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0),  # Cardinal directions
                (1, 1),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ]  # Diagonal directions

            for dx, dy in directions:
                new_x, new_y = self.x + dx, self.y + dy
                if (
                    0 <= new_x < self.environment.width
                    and 0 <= new_y < self.environment.height
                ):
                    if self.environment.grid[new_y][new_x] is None:
                        # Found an available location, create new organism here
                        return Organism(new_x, new_y, self.environment, new_genome)

            # If we get here, all adjacent locations were occupied, no reproduction
            return None

    def distance_from_organism_positive_x(self):
        for distance in range(1, self.environment.width - self.x):
            if self.environment.grid[self.y][self.x + distance] is not None:
                return distance
        return self.environment.width  # No organism in positive x direction

    def distance_from_organism_negative_x(self):
        for distance in range(1, self.x + 1):
            if self.environment.grid[self.y][self.x - distance] is not None:
                return distance
        return self.environment.width  # No organism in negative x direction

    def distance_from_organism_positive_y(self):
        for distance in range(1, self.environment.height - self.y):
            if self.environment.grid[self.y + distance][self.x] is not None:
                return distance
        return self.environment.height  # No organism in positive y direction

    def distance_from_organism_negative_y(self):
        for distance in range(1, self.y + 1):
            if self.environment.grid[self.y - distance][self.x] is not None:
                return distance
        return self.environment.height  # No organism in negative y direction

    def distance_from_wall_x(self):
        return min(self.x, self.environment.width - self.x)

    def distance_from_wall_y(self):
        return min(self.y, self.environment.height - self.y)

    def euclidean_distance_to_nearest_organism(self):
        min_distance = float("inf")
        nearest_organism = None

        for y in range(self.environment.height):
            for x in range(self.environment.width):
                organism = self.environment.grid[y][x]
                if organism is not None and organism != self:
                    dx = self.x - x
                    dy = self.y - y
                    distance = math.sqrt(dx * dx + dy * dy)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_organism = organism

        if nearest_organism is None:
            return None  # There are no other organisms in the environment
        else:
            return min_distance

    def color_of_nearest_organism(self):
        min_distance = float("inf")
        nearest_organism = None

        for y in range(self.environment.height):
            for x in range(self.environment.width):
                organism = self.environment.grid[y][x]
                if organism is not None and organism != self:
                    dx = self.x - x
                    dy = self.y - y
                    distance = math.sqrt(dx * dx + dy * dy)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_organism = organism

        if nearest_organism is None:
            return None  # There are no other organisms in the environment
        else:
            return nearest_organism.color
