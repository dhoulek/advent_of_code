# Advent of Code 2024, Day 6 Solution
# This script simulates a guard's path in a room grid, starting from a defined position.
# It calculates the number of tiles visited and identifies positions that would cause the guard to loop.

import numpy as np
from tqdm import tqdm  # For displaying progress in loops.

# Load the input file into a 2D NumPy array of characters.
# Each line becomes a row, forming the room grid.
room = np.array([list(l) for l in np.loadtxt('input.txt', dtype=str, comments=None)])

# Find the starting position of the guard, marked with '^'.
start_pos = np.where(room == '^')
y = start_pos[0][0]  # Row index of the starting position.
x = start_pos[1][0]  # Column index of the starting position.

# Function to simulate the guard's path in the room.
def check_path(room, return_path=False):
    """
    Simulates the guard's path in the room.

    Args:
        room (np.array): The 2D grid representing the room.
        return_path (bool): Whether to return the path of visited tiles.

    Returns:
        If return_path is True:
            visited (int): Number of visited tiles.
            tiles (list): List of coordinates of visited tiles.
        If return_path is False:
            visited (int): Number of visited tiles.
    """
    M, N = room.shape  # Dimensions of the room.
    dirs = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])  # Direction vectors (up, right, down, left).
    dir = 0  # Starting direction (up).
    visited = 1  # Count of visited tiles, starting with the initial position.

    # Locate the starting position ('^') in the room.
    start_pos = np.where(room == '^')
    y = start_pos[0][0]
    x = start_pos[1][0]
    room[y, x] = 'X'  # Mark the starting position as visited.
    steps = 1  # Step counter.

    if return_path:
        tiles = [[y, x]]  # Record visited tiles if return_path is True.

    out = False  # Flag to track if the guard exits the room.

    # Simulate the guard's movement.
    while not out and steps < M * N:  # Limit steps to prevent infinite loops.
        new_y = y + dirs[dir][0]  # Calculate the next row.
        new_x = x + dirs[dir][1]  # Calculate the next column.

        # Check if the next position is out of bounds.
        if not (0 <= new_y < M and 0 <= new_x < N):
            if return_path:
                tiles = np.transpose(np.where(room == 'X'))  # Get all visited tiles.
                return visited, tiles
            return visited
        else:
            if room[new_y, new_x] == '#':  # Wall encountered, change direction clockwise.
                dir = (dir + 1) % 4
            else:  # Move to the new position.
                y = new_y
                x = new_x
                if room[y, x] == '.':  # Count new tiles only if they are unvisited.
                    visited += 1
                    room[y, x] = 'X'  # Mark the tile as visited.
                steps += 1
    return -1  # Return -1 if the guard loops indefinitely.

# Step 1: Calculate the number of visited tiles and the path.
steps, positions = check_path(room.copy(), return_path=True)
print(f'Number of visited positions: {steps}')

# Deduplicate the positions (except the start position) to check for looping scenarios.
positions = np.unique(positions[1:], axis=0)

# Step 2: Check positions that would cause the guard to loop.
loops = 0  # Counter for positions causing loops.
for s in tqdm(positions):  # Use tqdm to show progress.
    if not (s[0] == start_pos[0][0] and s[1] == start_pos[1][0]):  # Exclude the starting position.
        r = room.copy()  # Create a fresh copy of the room.
        r[s[0], s[1]] = '#'  # Block the current position with a wall.
        steps = check_path(r)  # Simulate the guard's path with the modified room.
        if steps < 0:  # Check if the guard loops.
            loops += 1

# Output the number of positions causing the guard to loop.
print(f'Number of positions to make the guard loop: {loops}')