import numpy as np

# Read the entire file line-by-line, keeping raw spacing (important for column alignment).
lines = []
with open('input.txt') as f:
    for l in f.readlines():
        lines.append(l)

# The last line contains operation symbols (+ or *), one per problem.
# Split into a list, aligned left-to-right.
operations = lines.pop(-1).strip().split()

# Convert remaining lines into a 2D character array so we can rotate the worksheet.
# Each line becomes a list of characters (including spaces).
lines = np.array([list(l) for l in lines])

# Transpose the grid:
#   - Now each row (after transpose) corresponds to **one column** of the original worksheet.
#   - Reading columns top-to-bottom matches cephalopod digit order (most → least significant).
lines = lines.T

grand_total = 0
problem = []  # Stores the numbers belonging to the current problem (one per row/step in this column)

# Iterate over each column (left-to-right)
for l in lines:
    # Join the column's characters back into a string
    l = ''.join(l)
    
    # Strip whitespace — a non-empty result means this column has a number digit column
    l = l.strip()
    
    if len(l) > 0:
        # This column contains digits from top to bottom → one number for the current problem
        # Convert the digits to an integer and add it to the current problem list
        problem.append(int(l))
    else:
        # A fully blank column represents a separator between problems
        
        # Time to evaluate the *previous* problem
        op = operations.pop(0)  # Fetch the operation for this problem
        
        if op == '+':
            grand_total += np.sum(problem)
        else:
            grand_total += np.prod(problem)
        
        # Reset for the next problem
        problem = []

# Print final result. Note: The input always ends with a blank separator column,
# so the last problem gets evaluated inside the loop above.
print(f'Grand total is: {grand_total}')