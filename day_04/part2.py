import numpy as np

map = []
with open('input.txt') as f:
    for l in f.readlines():
        # Again convert each character:
        # '@' → 1 (roll of paper), '.' → 0 (empty)
        map.append([1 if i == '@' else 0 for i in l.strip()])

# Grid of rolls as a NumPy array
map = np.array(map)
N, M = map.shape

# `accessible` will store which rolls are accessible in each iteration.
# Start with a dummy non-zero array so that the while-loop runs at least once.
accessible = np.ones((N, M))

removed = 0  # Total number of rolls removed so far

# Keep looping as long as *any* rolls were accessible in the last iteration.
while np.sum(accessible) > 0:

    # Reset accessible map for this iteration
    accessible = np.zeros((N, M), dtype=int)

    # Check every cell in the grid
    for x in range(N):
        for y in range(M):

            # Only consider locations where a roll still exists
            if map[x, y] != 0:

                counts = 0  # Number of rolls in the 3×3 neighborhood

                # Count rolls in the 8 neighbors *including the center cell*.
                # Center cell has value 1, so total neighbors = counts - 1.
                for xx in range(x - 1, x + 2):
                    for yy in range(y - 1, y + 2):
                        if 0 <= xx < N and 0 <= yy < M:
                            counts += map[xx, yy]

                # In part two, a roll is removable if:
                #   1 ≤ total_in_3×3 ≤ 4
                # This corresponds to 0–3 neighbors in part 1,
                # but counts includes the roll itself, so:
                #   neighbors = counts - 1
                #   neighbors < 4  →  counts < 5
                # The condition is exactly your test: 1 <= counts < 5
                accessible[x, y] = 1 <= counts < 5

    # Remove all newly accessible rolls:
    # accessible contains 1s where rolls should be removed
    map = map - accessible

    # Count number of rolls removed in this iteration
    removed += np.sum(accessible)

# Final result
print(f'There are {removed} rolls of paper that can be accessed by a forklift.')