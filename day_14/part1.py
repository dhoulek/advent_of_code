# Advent of Code 2024 - Day 14: Part 1

import re

# Define the dimensions of the test bathroom or input space
# Uncomment for test input
# Lx, Ly = 11, 7

# Dimensions for the real input
Lx, Ly = 101, 103

# Number of steps to simulate
steps = 100

# Quadrant counters to track object positions
Q = [0, 0, 0, 0]

# Read input from the file and process each line
with open('input.txt', 'r') as f:
    for l in f.readlines():
        # Extract position and velocity values using a regular expression
        match = re.match(".*=(?P<x>-*\d+),(?P<y>-*\d+).*=(?P<vx>-*\d+),(?P<vy>-*\d+)", l)
        if match:
            # Parse matched values into integers
            x, y, vx, vy = (int(v) for v in match.groups())

            # Calculate the new position after the given number of steps
            X = (x + vx * steps) % Lx
            Y = (y + vy * steps) % Ly

            # Determine the quadrant of the new position and increment the counter
            if X < Lx // 2:
                if Y < Ly // 2:
                    Q[0] += 1  # Top-left quadrant
                elif Y > Ly // 2:
                    Q[1] += 1  # Bottom-left quadrant
            elif X > Lx // 2:
                if Y < Ly // 2:
                    Q[2] += 1  # Top-right quadrant
                elif Y > Ly // 2:
                    Q[3] += 1  # Bottom-right quadrant

# Calculate the safety factor as the product of the quadrant counters
safety_factor = 1
for v in Q:
    safety_factor *= v

# Output the safety factor
print(safety_factor)