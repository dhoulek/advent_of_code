import numpy as np

# Read the input file and store each line as an array of integers in 'seq'
seq = []
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    for l in f.readlines():
        seq.append(np.array([int(n) for n in l.strip().split()]))

# Lists to store extrapolated values on the right and left ends
extrapolated_right = []
extrapolated_left = []

# Loop through each sequence in 'seq'
for s in seq:
    # List to store differences at each step
    diffs = [s]
    
    # Continue until all elements in 's' become zero
    while not np.allclose(s, np.zeros(len(s))):
        # Calculate the differences between consecutive elements and append to 'diffs'
        s = s[1:] - s[:-1]
        diffs.append(s)
    
    # Initialize variables for extrapolation
    left = 0
    right = 0
    
    # Extrapolate values on the right end
    extrapolated_right.append(sum(d[-1] for d in reversed(diffs)))
    
    # Extrapolate values on the left end
    for d in reversed(diffs):
        right += d[-1]
        left = d[0] - left
    extrapolated_right.append(right)
    extrapolated_left.append(left)

# Print results for Part 1
print('Part 1:')
print(f'Sum of extrapolated values on the right end: {sum(extrapolated_right)}\n')

# Print results for Part 2
print('Part 2:')
print(f'Sum of extrapolated values on the left end: {sum(extrapolated_left)}')