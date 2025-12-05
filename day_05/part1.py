ranges = []      # List of fresh ID ranges (each as [low, high])
fresh_ids = []   # List of available ingredient IDs that are fresh

with open('input.txt') as f:
    range = True   # Indicates which section we are currently reading:
                   # True  = reading fresh ID ranges
                   # False = reading available ingredient IDs

    for l in f.readlines():
        l = l.strip()

        # A blank line switches from range-section to ID-section
        if len(l) == 0:
            range = False

        else:
            if range:
                # Still reading the fresh ID ranges before the blank line
                # Convert "a-b" into [a, b]
                ranges.append([int(i) for i in l.split('-')])

            else:
                # Reading the available ingredient IDs (after the blank line)
                id = int(l)

                # Check whether this ID falls into ANY of the given ranges
                for r in ranges:
                    if r[0] <= id <= r[1]:
                        # As soon as we find one matching range,
                        # we know the ingredient is fresh
                        fresh_ids.append(id)
                        break  # Do not check other ranges

# The answer is simply the number of IDs determined to be fresh
print(f'Number of available ingredient IDs that are fresh: {len(fresh_ids)}')