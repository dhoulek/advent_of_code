"""
Advent of Code 2024
Day 15, Part 1: Robot Navigation in a Warehouse

Description:
This script simulates a robot navigating a warehouse grid based on a series of instructions. The warehouse
layout and instructions are read from an input file. The goal is to determine the sum of all GPS coordinates
of the 'O' boxes after the robot completes its movements.
"""

import numpy as np

# Initialize the warehouse and instructions list
warehouse = []
instructions = []

# Boolean to switch between reading the warehouse map and instructions
reading_map = True

# Read input from 'input.txt'
with open('input.txt', 'r') as f:
    for l in f.readlines():
        l = l.strip()  # Remove leading and trailing whitespace
        if len(l) == 0:
            # An empty line separates the warehouse map and instructions
            reading_map = False
        else:
            if reading_map:
                # Append each row of the warehouse to the list
                warehouse.append(list(l))
            else:
                # Collect all instructions
                instructions += list(l)

# Convert the warehouse list into a NumPy array for easier manipulation
warehouse = np.array(warehouse)

# Locate the robot's initial position (marked with '@')
robot = np.array([a[0] for a in np.where(warehouse == '@')])

# Replace the robot's position in the warehouse with an empty space ('.')
warehouse[robot[0], robot[1]] = '.'

# Function to print the warehouse grid with the robot's current position
def print_warehouse(warehouse, robot):
    w = warehouse.copy()
    w[robot[0], robot[1]] = '@'  # Mark the robot's position
    for l in w:
        print(''.join(l))

# Define movement directions as vectors
dirs = {
    '^': np.array([-1, 0]),  # Up
    '>': np.array([0, 1]),   # Right
    '<': np.array([0, -1]),  # Left
    'v': np.array([1, 0]),   # Down
}

# Function to recursively move the robot
def move_robot(warehouse, position, dir):
    # Check if the current position is a wall
    if warehouse[position[0], position[1]] == '#':
        return False
    # Check if the current position is empty
    elif warehouse[position[0], position[1]] == '.':
        return True
    else:
        # Move to the next position based on the direction
        new_pos = position + dirs[dir]
        if move_robot(warehouse, new_pos, dir):
            # Update the warehouse with the robot's trail
            warehouse[new_pos[0], new_pos[1]] = warehouse[position[0], position[1]]
            warehouse[position[0], position[1]] = '.'
            return True
        else:
            return False

# Uncomment these lines for debugging purposes
# print(instructions)
# print_warehouse(warehouse, robot)

# Execute each instruction to move the robot
for i, move in enumerate(instructions):
    moved = move_robot(warehouse, robot + dirs[move], move)
    if moved:
        robot = robot + dirs[move]
    # Uncomment for step-by-step debugging
    # print(f'Step {i}: {move}; robot={robot}')
    # print_warehouse(warehouse, robot)

# Calculate the GPS coordinates of all 'O' boxes in the warehouse
GPS = [sum(a) for a in np.where(warehouse == 'O')]
GPS = 100 * GPS[0] + GPS[1]

# Output the result
print(f'Sum of all boxes' GPS coordinates: {GPS}')