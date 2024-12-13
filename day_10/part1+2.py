# Advent of Code - Day 10 Solution
# This script processes a grid of numbers (0-9) to determine:
# 1. The total number of unique endpoints reachable from each starting '0' tile via valid trails.
# 2. The total number of valid trails.
# Trails must progress sequentially from '0' to '9', moving only between adjacent tiles.

import cmath  # For complex number operations to represent positions on a grid.
from tqdm import tqdm  # Progress bar utility for iterations.

# Initialize a dictionary to store the positions of tiles for each number (0-9).
tiles = {i: [] for i in range(10)}

# Read input file and populate the `tiles` dictionary with positions (x + y*1j).
with open('input.txt', 'r') as f:
    for y, line in enumerate(f.readlines()):  # Loop through each line (row index y).
        for x, n in enumerate(line.strip()):  # Loop through each character in the line (column index x).
            tiles[int(n)].append(x + y * 1j)  # Store the tile position as a complex number.

# Initialize trails, starting with the positions of all '0' tiles.
trails = [[X] for X in tiles[0]]

# Build trails from '0' through '9', ensuring each step connects adjacent tiles.
for i in tqdm(range(1, 10)):  # Iterate through numbers 1 to 9.
    longer = []  # Temporary list to hold extended trails.
    for trail in trails:  # For each current trail...
        X = trail[-1]  # Get the last tile in the trail.
        for Y in tiles[i]:  # Check all positions of the current number `i`.
            if abs(X - Y) == 1.0:  # Check if the tile `Y` is adjacent to the last tile `X`.
                longer.append(trail + [Y])  # Extend the trail with `Y`.
    trails = longer.copy()  # Update trails with the extended versions.

# Calculate scores for each starting position of a '0' tile.
scores = {X: set() for X in tiles[0]}  # Initialize scores for each '0' position.
for trail in trails:  # For each valid trail...
    scores[trail[0]].add(trail[-1])  # Record the endpoint of the trail in the scores.

# Compute the total score as the sum of unique endpoints for each starting position.
score_sum = sum([len(s) for s in scores.values()])
print("The map's score is:", score_sum)  # Output the total score.

# Compute the rating as the total number of valid trails.
rating = len(trails)
print("The map's rating is:", rating)  # Output the rating.