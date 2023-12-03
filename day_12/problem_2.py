import numpy as np
from tqdm import tqdm

heights = []
with open('input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()        
        if 'E' in line:
            j = line.index('E')
            final = (i, j)
        line = line.replace('S', 'a')
        line = line.replace('E', 'z')
        heights.append([ord(x)-ord('a') for x in line])


heights = np.array(heights)
m, n = heights.shape

min_dist = m*n

# in comparison to problem 1, we have many more starting positions now
starting = np.where(heights == 0)
tasks = tqdm(zip(*starting))


# go through all starting positions, but otherwise keep the implementation
# from problem 1
for sx, sy in tasks:
    tasks.set_description(f'min dist {min_dist}')
    
    paths = np.array([None]*(m*n)).reshape(m, n)
    paths[sx, sy] = 0
    # print(paths)

    for l in range(m*n):
        # get position where I can get in `l` steps
        pos = np.where(paths == l)
        # go through these positions and check to which NN I can go
        for i, j in zip(*pos):
            # my height
            h = heights[i, j]
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                if (0 <= i+x < m) and (0 <= j+y < n):
                    if paths[i+x, j+y] == None and heights[i+x, j+y] <= h+1:
                        paths[i+x, j+y] = l+1
            if (i, j) == final:
                break
    if paths[final] != None and paths[final] < min_dist:
        min_dist = paths[final]

# print(paths)
print('\nMinimum path length is', min_dist)