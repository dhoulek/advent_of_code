# Advent of Code 2024, Day 8 Solution
# This script calculates unique "antinodes" based on antenna positions 
# in a 2D grid and performs computations with harmonics.

from itertools import combinations  # For generating pairs of antenna coordinates.

# Initialize grid dimensions and antenna dictionary.
M, N = 0, 0  # `M` and `N` represent the grid dimensions (columns and rows).
antennas = dict()  # Stores antennas and their positions as complex numbers.

# Read the input file to extract antenna positions.
with open('input.txt', 'r') as f:
    for y, line in enumerate(f.readlines()):  # Iterate through lines of the file.
        for x, c in enumerate(line.strip()):  # Iterate through characters in each line.
            N = max(N, y)  # Update the row (N) dimension.
            M = max(M, x)  # Update the column (M) dimension.
            if c != '.':  # If the character is not a dot ('.'), it's an antenna.
                if c not in antennas.keys():  # Initialize list for this antenna type.
                    antennas[c] = list()
                antennas[c].append(x + y * (1j))  # Store position as a complex number.

# Calculate antinodes (positions derived from antenna pairs).
antinodes = []
for ant in antennas:  # For each type of antenna.
    for z1, z2 in combinations(antennas[ant], 2):  # Generate all pairs of antenna positions.
        for node in [2 * z1 - z2, 2 * z2 - z1]:  # Calculate potential antinodes.
            if 0 <= node.real <= M and 0 <= node.imag <= N:  # Check if within grid bounds.
                antinodes.append(node)  # Add valid antinode positions to the list.

# Output the number of unique antinodes.
print(f'Number of unique antinodes: {len(set(antinodes))}')

# Calculate antinodes considering all harmonics.
antinodes = []
for ant in antennas:  # For each type of antenna.
    for z1, z2 in combinations(antennas[ant], 2):  # Generate all pairs of antenna positions.
        for node in [z1 + m * (z1 - z2) for m in range(-M - 1, M + 1)]:  # Calculate positions for harmonics.
            if 0 <= node.real <= M and 0 <= node.imag <= N:  # Check if within grid bounds.
                antinodes.append(node)  # Add valid antinode positions to the list.

# Output the number of unique antinodes considering harmonics.
print(f'Number of unique antinodes with all harmonics: {len(set(antinodes))}')