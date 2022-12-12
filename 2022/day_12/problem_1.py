import numpy as np

heights = []
paths = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        paths.append([0 if x=='S' else None for x in line])
        if 'E' in line:
            j = line.index('E')
            final = (i, j)
        line = line.replace('S', 'a')
        line = line.replace('E', 'z')
        heights.append([ord(x)-ord('a') for x in line])

heights = np.array(heights)
paths = np.array(paths)
# print(heights)
# print(paths)

m, n = heights.shape
for l in range(m*n):
    # get position where I can get in `l` steps
    pos = np.where(paths == l)
    # go through these positions and check to which NN I can go
    for i, j in zip (*pos):
        # my height
        h = heights[i, j]
        for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            if (0 <= i+x < m) and (0 <= j+y < n):
                if paths[i+x, j+y] == None and heights[i+x, j+y] <= h+1:
                    paths[i+x, j+y] = l+1
        if (i, j) == final:
            break

# print(paths)
print('Minimum path length is', paths[final])