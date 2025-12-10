splits = 0                 # Count of total beam splits
initialized = False        # Tracks whether we've processed the top row (the row with S)

with open('input.txt') as f:
    for l in f.readlines():

        # Convert row of characters to a list and strip trailing newline
        l = list(l.strip())

        if initialized:
            # We have already processed the first row; now simulate beam movement to next row

            # Placeholder for beams in the new row (0 = no beam, 1 = beam present)
            new_row = [0] * len(row)

            for i in range(len(l)):

                # If a beam is present at this column from the row above:
                if row[i] == 1:

                    if l[i] == '^':
                        # Beam hits a splitter: split left/right instead of continuing downward
                        splits += 1

                        # Emit beam to the left (if inside grid)
                        if i > 0:
                            new_row[i - 1] = 1

                        # Emit beam to the right (if inside grid)
                        if i < len(row) - 1:
                            new_row[i + 1] = 1

                    else:
                        # Beam travels straight downward into the same column
                        new_row[i] = 1

            # Move to next row: current beams become new_row
            row = new_row

        else:
            # First row: initialize beam positions
            # Beam starts at the location marked 'S'
            row = [1 if x == 'S' else 0 for x in l]
            initialized = True

# Final output
print(f'Number of a tachyon beam splits: {splits}')