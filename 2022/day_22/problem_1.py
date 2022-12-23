import numpy as np

inp = 'test'
with open(f'{inp}.path') as f:
    path = f.readline().strip()
# get max line length
max_length = 0
inp_data = []
with open(f'{inp}.map') as f:
    for line in f.readlines():
        line = line[:-1]
        max_length = max(max_length, len(line))
        inp_data.append(line)
board = np.zeros((len(inp_data), max_length), dtype=np.int0)
for i, line in enumerate(inp_data):
    for j, c in enumerate(line):
        if c == '.':
            board[i, j] = 1
        elif c == '#':
            board[i, j] = 2
# get row and column limits
# note that the inaccessible parts (0) are always at the beggining or end of
# rows and columns
rows = []
columns = []
for i in range(board.shape[0]):
    left = 0
    while board[i, left] == 0:
        left += 1
    right = board.shape[1]-1
    while board[i, right] == 0:
        right -= 1
    rows.append((left, right))
    
for j in range(board.shape[1]):
    top = 0
    while board[top, j] == 0:
        top += 1
    bottom = board.shape[0]-1
    while board[bottom, j] == 0:
        bottom -= 1
    columns.append((top, bottom))
    
print(rows, columns)