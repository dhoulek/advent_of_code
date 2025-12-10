# Read the manifold diagram into a 2D list of characters
manifold = []
with open('input.txt') as f:
    for l in f.readlines():
        manifold.append(list(l.strip()))

# timelines[i] = how many timelines contain a tachyon particle
# that arrives at column i of the *current row*.
# Initialization: only position of 'S' contains 1 timeline, all others 0.
timelines = [1 if x == 'S' else 0 for x in manifold[0]]

# Process each subsequent row of the manifold
for row in manifold[1:]:

    # Prepare an empty next-row timeline counter
    new = [0 for _ in range(len(row))]

    # For every column in the current row:
    for i in range(len(row)):

        # If a splitter '^' is present:
        if row[i] == '^':
            # The particle's timeline splits:
            # all timelines arriving at (row,i) produce:
            # - a new timeline moving left, if inside bounds
            if i > 0:
                new[i - 1] += timelines[i]

            # - a new timeline moving right, if inside bounds
            if i < len(row) - 1:
                new[i + 1] += timelines[i]

        else:
            # Otherwise, space is empty ('.'):
            # timelines pass straight downward into the same column
            new[i] += timelines[i]

    # Move down to the next row
    timelines = new

# The total number of distinct timelines is the sum of all particle locations
print(f'Number of a timelines of tachyom beam: {sum(timelines)}')