# environment.py
import matplotlib.pyplot as plt


class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    def add_organism(self, organism):
        self.grid[organism.y][organism.x] = organism

    def remove_organism(self, organism):
        self.grid[organism.y][organism.x] = None

    def step(self):
        # Define what happens each time step here
        pass

    def plot(self, step):
        plt.figure(figsize=(6, 6))
        plt.xlim(0, self.width)
        plt.ylim(0, self.height)
        plt.title(f"Time Step: {step}")

        for y in range(self.height):
            for x in range(self.width):
                organism = self.grid[y][x]
                if organism is not None:
                    plt.plot(x, y, "o")

        plt.pause(0.1)  # display the window for 1 second and then close it
        plt.clf()  # clear the figure for the next plot
