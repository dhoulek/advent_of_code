import numpy as np

# Initialize lists to store galaxy positions and their impact on rows and columns
galaxies = []
row_values = []
col_values = []

# Read input from a file named 'input.txt'
with open('input.txt', 'r') as f:
    y = 0
    for l in f.readlines():
        if col_values == []:
            # Initialize column values with 2 (indicating empty space)
            col_values = [2]*len(l.strip())
        if '#' in l:
            # If '#' is present in the line, mark the row as 1 and update the galaxies list
            row_values.append(1)
            for x in range(len(l.strip())):
                if l[x] == '#':
                    galaxies.append([y, x])
                    # Update column values to mark the presence of a galaxy (1)
                    col_values[x] = 1
        else:
            # If '#' is not present, mark the row as 2
            row_values.append(2)
        y += 1

# Convert row and column values to numpy arrays
row_values = np.array(row_values)
col_values = np.array(col_values)

# Calculate distances between galaxies in Part 1
dist = []
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        ymin = min(g1[0], g2[0])
        ymax = max(g1[0], g2[0])
        xmin = min(g1[1], g2[1])
        xmax = max(g1[1], g2[1])
        # Calculate distance by summing the values in the specified ranges
        d = sum(row_values[ymin: ymax]) + sum(col_values[xmin: xmax])
        dist.append(d)

# Print the result for Part 1
print('Part 1:')
print(f'Sum of distances between galaxies: {sum(dist)}\n')

# Modify column and row values for Part 2
col_values = (col_values - 1) * 999999 + 1
row_values = (row_values - 1) * 999999 + 1

# Calculate distances between galaxies in Part 2
dist = []
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        g1 = galaxies[i]
        g2 = galaxies[j]
        ymin = min(g1[0], g2[0])
        ymax = max(g1[0], g2[0])
        xmin = min(g1[1], g2[1])
        xmax = max(g1[1], g2[1])
        # Calculate distance by summing the modified row and column values
        d = sum(row_values[ymin: ymax]) + sum(col_values[xmin: xmax])
        dist.append(d)

# Print the result for Part 2
print('Part 2:')
print(f'Sum of distances between very old galaxies: {sum(dist)}')