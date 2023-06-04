# visualization.py
import matplotlib.pyplot as plt


def plot_environment(environment):
    plt.figure(figsize=(6, 6))
    plt.xlim(0, environment.width)
    plt.ylim(0, environment.height)

    for y in range(environment.height):
        for x in range(environment.width):
            organism = environment.grid[y][x]
            if organism is not None:
                plt.plot(x, y, "o")  # plot a point at (x, y)

    plt.show()
