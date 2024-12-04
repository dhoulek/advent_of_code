# Advent of Code 2024, Day 4 Solution
# This script analyzes a crossword-like grid to count occurrences of specific patterns
# ("XMAS" and "SAMX") in rows, columns, and diagonals, as well as special "X-MAS" patterns.

import numpy as np

# Load the input into a NumPy 2D array of characters.
# Each line from the file becomes a list of characters, forming the grid.
xword = np.array([list(l) for l in np.loadtxt('input.txt', dtype=str)])

# Part 1: Count the occurrences of "XMAS": horizontal, vertical, diagonal, written backwards
count = 0
M, N = xword.shape  # Dimensions of the crossword grid.

# Check for patterns in rows.
for i in range(M):
    for j in range(N - 3):  # Ensure there are at least 4 characters remaining in the row.
        word = ''.join(xword[i, j:j+4])  # Extract a substring of 4 characters.
        if word == 'XMAS' or word == 'SAMX':  # Check for matching patterns.
            count += 1

# Check for patterns in columns.
for i in range(M - 3):  # Ensure there are at least 4 rows remaining.
    for j in range(N):
        word = ''.join(xword[i:i+4, j])  # Extract a vertical substring of 4 characters.
        if word == 'XMAS' or word == 'SAMX':  # Check for matching patterns.
            count += 1

# Check for patterns in diagonals.
for i in range(M - 3):
    for j in range(N - 3):
        # Check the main diagonal (top-left to bottom-right).
        word = ''.join([xword[i+k, j+k] for k in range(4)])
        if word == 'XMAS' or word == 'SAMX':
            count += 1
        # Check the anti-diagonal (top-right to bottom-left).
        word = ''.join([xword[i+3-k, j+k] for k in range(4)])
        if word == 'XMAS' or word == 'SAMX':
            count += 1

# Output the total count of "XMAS" and "SAMX".
print(f'Number of XMAS appearances: {count}')

# Part 2: Count the occurrences of "X-MAS" patterns.
count = 0
for i in range(M - 2):  # Ensure there are at least 3 rows remaining.
    for j in range(N - 2):  # Ensure there are at least 3 columns remaining.
        # Check the main diagonal (3 characters).
        diag1 = ''.join([xword[i+k, j+k] for k in range(3)])
        # Check the anti-diagonal (3 characters).
        diag2 = ''.join([xword[i+2-k, j+k] for k in range(3)])
        # Verify the "MAS" or "SAM" condition for both diagonals.
        if (diag1 == 'MAS' or diag1 == 'SAM') and (diag2 == 'MAS' or diag2 == 'SAM'):
            count += 1

# Output the total count of "X-MAS" patterns.
print(f'Number of X-MAS appearances: {count}')