import numpy as np

inp = 'input'
path  =[]
with open(f'{inp}.path') as f:
    n =''
    for c in f.readline().strip():
        if c.isnumeric():
            n += c
        else:
            path += [int(n), c]
            n = ''
    if n != '':
        path += [int(n)]
print(path)
    
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

print(board.shape)
print(rows)
print(columns)

def read(pos):
    return board[tuple(pos)]

def new(pos, dir):
    new_pos = np.array(pos) + moves[dir]
    # print(f'  . new position: {new_pos}')
    if dir == 0:
        # horizontal move, check range
        if new_pos[1] > rows[pos[0]][1]:
            new_pos[1] = rows[pos[0]][0]
    elif dir == 2:
        # horizontal move, check range
        if new_pos[1] < rows[pos[0]][0]:
            new_pos[1] = rows[pos[0]][1]
    elif dir == 1:
        # vertical move, check range
        if new_pos[0] > columns[pos[1]][1]:
            new_pos[0] = columns[pos[1]][0]
    elif dir == 3:
        # vertical move, check range
        if new_pos[0] < columns[pos[1]][0]:
            new_pos[0] = columns[pos[1]][1]
    # print(f'  + wrapped new position: {new_pos}')
    return new_pos
    

moves = [(0,1), (1,0), (0,-1), (-1,0)]
pos = np.array([0, rows[0][0]])
dir = 0
print(f'starting position: {pos} in direction {moves[dir]}')

for i in path:
    if i == 'L':
        dir = (dir-1) % 4
    elif i == 'R':
        dir = (dir+1) % 4
    else:
        for _ in range(i):
            new_pos = new(pos, dir)
            if read(new_pos) == 1:
                pos = new_pos
            else:
                break
    print(f'after {i} at position: {pos} in direction {moves[dir]}')
    
print(f'final score: {1000*(pos[0]+1)+4*(pos[1]+1)+dir}')

