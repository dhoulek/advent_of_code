import numpy as np
from tqdm import tqdm

# Define directions for movement
dirs = {
    '>': np.array([0, 1]),
    '<': np.array([0, -1]),
    'A': np.array([-1, 0]),
    'V': np.array([1, 0]),
}

# Define mirrors for '/' and '\'
mirror_left = {'>': 'V', '<': 'A', 'A': '<', 'V': '>'}
mirror_right = {'>': 'A', '<': 'V', 'A': '>', 'V': '<'}


def propagate(ends):
    def add(y, x, d):
        if 0 <= y < n and 0 <= x < m:
            new_ends.append([(y, x), d])

    new_ends = []
    for e in ends:
        p, d = e
        y, x = p
        if d not in visited[y][x]:
            # First time here with this direction -> propagate
            visited[y][x] += d
            if layout[y, x] == '/':
                d = mirror_right[d]
                y, x = np.array(p) + dirs[d]
                add(y, x, d)
            elif layout[y, x] == '\\':
                d = mirror_left[d]
                y, x = np.array(p) + dirs[d]
                add(y, x, d)
            elif layout[y, x] == '|' and d in ['>', '<']:
                add(y - 1, x, 'A')
                add(y + 1, x, 'V')
            elif layout[y, x] == '-' and d in ['A', 'V']:
                add(y, x - 1, '<')
                add(y, x + 1, '>')
            else:
                y, x = np.array(p) + dirs[d]
                add(y, x, d)
    return new_ends

# Read input layout from file
layout = []
with open('input.txt', 'r') as f:
    for l in f.readlines():
        layout.append(np.array(list(l.strip())))
layout = np.array(layout)
n, m = layout.shape
visited = [['' for j in range(m)] for i in range(n)]

# Part 1: Propagate from the top-left corner
ends = [[(0, 0), '>']]
while len(ends) > 0:
    ends = propagate(ends)

# Count energized tiles in Part 1
energized = 0
for l in visited:
    for p in l:
        if len(p) > 0:
            energized += 1
print('Part 1:')
print(f'Number of energized tiles: {energized}\n')

# Part 2: Propagate from each starting point on the borders
energized_max = 0
starts = [[(0, mm), 'V'] for mm in range(m)]
starts += [[(n - 1, mm), 'A'] for mm in range(m)]
starts += [[(nn, m - 1), '<'] for nn in range(n)]
starts += [[(nn, 0), '>'] for nn in range(n)]
for s in tqdm(starts):
    ends = [s]
    visited = [['' for j in range(m)] for i in range(n)]
    while len(ends) > 0:
        ends = propagate(ends)
    energized = 0
    for l in visited:
        for p in l:
            if len(p) > 0:
                energized += 1
    energized_max = max(energized_max, energized)

print('Part 2:')
print(f'Maximum number of energized tiles: {energized_max}')