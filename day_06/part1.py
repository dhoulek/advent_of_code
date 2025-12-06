import numpy as np

# Read the worksheet into a list of rows, each row split by whitespace
numbers = []
with open('input.txt') as f:
    for l in f.readlines():
        # Each row contains the numbers for all problems in that row
        numbers.append(l.strip().split())

# The last row contains the operations (+ or *) for each problem
operations = numbers.pop(-1)

# Convert the remaining rows (the numbers) into a NumPy array of integers
# After this, each row is one horizontal slice of the worksheet
numbers = np.array(numbers, dtype=int)

# Transpose the array so that:
#   – each column corresponds to one full problem
#   – each problem is a list of vertical numbers
numbers = numbers.T

grand_total = 0
# Iterate simultaneously over each vertical problem and its operation
for problem, op in zip(numbers, operations):
    # Sum or multiply depending on the operation symbol
    if op == '+':
        grand_total += np.sum(problem)
    else:
        grand_total += np.prod(problem)

# Output the combined total of all problem results
print(f'Grand total is: {grand_total}')