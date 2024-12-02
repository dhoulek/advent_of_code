# Advent of Code 2024, Day 1 Solution
# This script calculates the total distance and similarity index between two columns of integers 
# from an input text file.

import numpy as np

# Load the input data from 'input.txt', assuming it contains two columns of integers.
# Each row represents a pair of values.
data = np.loadtxt('input.txt', dtype=np.int64)

# Extract the first column (col1) and sort it.
col1 = data[:, 0]
col1.sort()

# Extract the second column (col2) and sort it.
col2 = data[:, 1]
col2.sort()

# Calculate the total distance between the two sorted columns.
# The distance is the sum of the absolute differences between corresponding elements.
total_distance = np.sum(np.abs(col1 - col2))
print(f'Total distance between the two entry lists is: {total_distance}')

# Create a dictionary to count occurrences of each value in col2.
occ = dict()
for v in col2:
    if v in occ.keys():
        occ[v] += 1
    else:
        occ[v] = 1

# Calculate the similarity index based on col1 and the occurrence dictionary of col2.
# For each value in col1, if it exists in the dictionary, 
# multiply the value by its count in col2 and add to the similarity index.
similarity_index = 0
for v in col1:
    if v in occ.keys():
        similarity_index += v * occ[v]

print(f'Similarity index is {similarity_index}')