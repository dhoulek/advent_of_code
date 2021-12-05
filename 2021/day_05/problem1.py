import numpy as np
from numpy.core.numeric import cross

input = []
num_lines = 0
max_x = 0
max_y = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        num_lines += 1
        first = line.split(' ')[0]
        x1, y1 = [int(n) for n in  first.split(',')]
        second = line.split(' ')[-1]
        x2, y2 = [int(n) for n in second.split(',')]
        max_x = max([max_x, x1, x2])
        max_y = max([max_y, y1, y2])
        if x1 == x2 or y1 == y2:
            input.append([x1, y1, x2, y2])
print(f'read in total {num_lines} input lines')
print(f'but only {len(input)} horizontal/vertical lines')
print(f'maximum coordinates are x={max_x}, y={max_y}')

max_x += 1
max_y += 1

board = np.zeros(max_x*max_y, dtype=int).reshape(max_y, max_x)

for x1, y1, x2, y2 in input:
    # print(x1, y1, x2, y2)
    if x1 == x2:
        # print('vertical')
        for c in np.arange(min(y1, y2), max(y1, y2)+1):
            board[c][x1] += 1
    if y1 == y2:
        # print('horizontal')
        for c in np.arange(min(x1, x2), max(x1, x2)+1):
            board[y1][c] += 1

# print(board)
crosses = 0
for v in board.flatten():
    if v > 1:
        crosses += 1
print(f'number of crosses = {crosses}')