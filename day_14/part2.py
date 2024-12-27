# Advent of Code 2024 - Day 14: Part 2

import re
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# Define the dimensions of the simulation space
Lx, Ly = 101, 103

# Number of steps to simulate for plotting
steps = 2000

# Lists to store initial positions and velocities
positions = []
velocities = []

# Read input from the file and extract position and velocity data
with open('input.txt', 'r') as f:
    for l in f.readlines():
        # Use a regular expression to parse the input data
        match = re.match(".*=(?P<x>-*\d+),(?P<y>-*\d+).*=(?P<vx>-*\d+),(?P<vy>-*\d+)", l)
        if match:
            x, y, vx, vy = (int(v) for v in match.groups())
            positions.append([x, y])  # Add position to the list
            velocities.append([vx, vy])  # Add velocity to the list

# Transpose helper function to separate x and y coordinates
trans = lambda l: list(map(list, zip(*l)))

# Steps for visualization (can use a range or specific steps)
# Uncomment for dynamic exploration
# for i in tqdm(np.arange(28, 10000, 103)):
# for i in tqdm(np.arange(55, 10000, 101)):

# Plot and save the visualization for a specific step
for i in [6620]:
    new_positions = []

    # Update positions based on velocity and step count
    for p, v in zip(positions, velocities):
        new_positions.append([(p[0] + i * v[0]) % Lx, (p[1] + i * v[1]) % Ly])

    # Transpose positions for plotting
    pos = trans(new_positions)

    # Plot the positions
    plt.plot(*pos, '.')
    plt.xlim(0, Lx)
    plt.ylim(0, Ly)
    plt.title(f'Step: {i}')

    # Save the plot as a PNG file
    plt.savefig(f'step_{i:08d}.png')
    plt.close()