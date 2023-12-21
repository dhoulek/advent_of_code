import numpy as np

dirs = {
    '>': np.array([0, 1]),
    '<': np.array([0, -1]),
    'A': np.array([-1, 0]),
    'V': np.array([1, 0]),
    }
# \
mirror_left = {'>': 'V', '<': 'A', 'A': '<', 'V': '>'}
# /
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
            # first time here with this direction -> propagate
            visited[y][x] += d
            # count[y, x] += 1
            if layout[y, x] == '/':
                d = mirror_right[d]
                y, x = np.array(p)+dirs[d]
                add(y, x, d)
            elif layout[y, x] == '\\':
                d = mirror_left[d]
                y, x = np.array(p)+dirs[d]
                add(y, x, d)
            elif layout[y, x] == '|' and d in ['>', '<']:
                add(y-1, x, 'A')
                add(y+1, x, 'V')
            elif layout[y, x] == '-' and d in ['A', 'V']:
                add(y, x-1, '<')
                add(y, x+1, '>')
            else:
                y, x = np.array(p)+dirs[d]
                add(y, x, d)
    return new_ends

layout = []
with open('input.txt', 'r') as f:
    for l in f.readlines():
        layout.append(np.array(list(l.strip())))
layout = np.array(layout)
n, m = layout.shape
visited = [['' for j in range(m)] for i in range(n)]
# count = np.array([np.array([0 for j in range(m)]) for i in range(n)])




ends = [[(0,0), '>']]
# i = 0
while len(ends) > 0:
    # i += 1 
    ends = propagate(ends)


# for l in visited:
#     s = ''
#     for p in l:
#         if len(p) == 0:
#             s += '.'
#         elif len(p) > 1:
#             s += str(len(p))
#         else:
#             s += p
#     # print(s)
# # print(visited)
energized = 0
for l in visited:
    for p in l:
        if len(p) > 0:
            energized += 1
print('Part 1:')
print(energized)