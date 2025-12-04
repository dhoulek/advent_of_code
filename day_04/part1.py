import numpy as np

map = []
with open('input.txt') as f:
    for l in f.readlines():
        # Convert each line into a list of 1s and 0s:
        # 1 = roll of paper '@'
        # 0 = empty space '.'
        map.append([1 if i == '@' else 0 for i in l.strip()])

# Convert the list of lists to a NumPy array for easy indexing
map = np.array(map)
N, M = map.shape  # Grid dimensions

accessible = 0  # Count of rolls accessible by a forklift

for x in range(N):
    for y in range(M):

        # Only consider cells that actually contain a roll of paper
        if map[x, y] != 0:

            counts = -1  
            # Start at -1 so that when looping over the 3×3 area below,
            # we subtract out the center cell — because map[x,y] == 1,
            # and we want to count only the NEIGHBOR rolls (not itself).

            # Loop over all neighbors in the 8 surrounding positions
            for xx in range(x - 1, x + 2):       # x-1, x, x+1
                for yy in range(y - 1, y + 2):   # y-1, y, y+1

                    # Only count valid positions inside the grid
                    if 0 <= xx < N and 0 <= yy < M:
                        counts += map[xx, yy]  # Add 1 for rolls '@', 0 for empty

            # A forklift can access this roll if it has *fewer than 4* adjacent rolls
            # `0 <= counts < 4` evaluates to True (1) or False (0), so add it.
            accessible += 0 <= counts < 4

print(f'There are {accessible} rolls of paper that can be accessed by a forklift.')