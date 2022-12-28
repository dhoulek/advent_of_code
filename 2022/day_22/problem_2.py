import numpy as np

moves = [(0,1), (1,0), (0,-1), (-1,0)]

inp = 'test'
side = 4
pos = np.array([0, 2*side])
shape = np.array([[0, 0, 1, 0], 
                  [2, 3, 4, 0], 
                  [0, 0, 5, 6]])

neighbours = {1: [6, 4, 3, 2],
              2: [3, 5, 6, 1],
              3: [4, 5, 2, 1],
              4: [6, 5, 3, 1],
              5: [6, 2, 3, 4],
              6: [1, 2, 5, 4]
             }
new_direction = {1: [2, 1, 1, 1],
                 2: [0, 3, 3, 1],
                 3: [0, 0, 2, 0],
                 4: [1, 1, 2, 3],
                 5: [0, 3, 3, 3],
                 6: [2, 0, 2, 2]
                 }

inp = 'input'
side = 50
pos = np.array([0, side])
shape = np.array([[0, 1, 2], 
                  [0, 3, 0], 
                  [4, 5, 0],
                  [6, 0, 0]])
neighbours = {1: [2, 3, 4, 6],
              2: [5, 3, 1, 6],
              3: [2, 5, 4, 1],
              4: [5, 6, 1, 3],
              5: [2, 6, 4, 3],
              6: [5, 2, 1, 4]
             }
new_direction = {1: [0, 1, 0, 0],
                 2: [2, 2, 2, 3],
                 3: [3, 1, 1, 3],
                 4: [0, 1, 0, 0],
                 5: [2, 2, 2, 3],
                 6: [3, 1, 1, 3]
                 }

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


def read(pos):
    return board[tuple(pos)]

def new(pos, dir):    
    new_pos = np.array(pos) + moves[dir]
    # do we stay on the same side?    
    if get_side(new_pos) == get_side(pos):
        # yes - return new position
        return new_pos, dir
    else:        
        # no - figure out how we transfer to a neighboring side
        # index of the side on board
        new_side = tuple([v[0] for v in np.where(shape == neighbours[get_side(pos)][dir])])
        # rotation
        new_dir = new_direction[get_side(pos)][dir]
        if dir == 0:
            if new_dir == 1:
                new_pos = np.array([side*new_side[0],                             side*(new_side[1]+1)-1 - get_rel_pos(pos)[0]])
            elif new_dir == 0:
                new_pos = np.array([side*new_side[0]       + get_rel_pos(pos)[0], side*new_side[1]])
            elif new_dir == 2:
                new_pos = np.array([side*(new_side[0]+1)-1 - get_rel_pos(pos)[0], side*(new_side[1]+1)-1])
            elif new_dir == 3:
                new_pos = np.array([side*(new_side[0]+1)-1,                       side*new_side[1]       + get_rel_pos(pos)[0]])
        elif dir == 1:
            if new_dir == 1:
                new_pos = np.array([side*new_side[0],                             side*new_side[1]       + get_rel_pos(pos)[1]])
            elif new_dir == 0:
                new_pos = np.array([side*(new_side[0]+1)-1 - get_rel_pos(pos)[1], side*new_side[1]])
            elif new_dir == 2:
                new_pos = np.array([side*new_side[0]       + get_rel_pos(pos)[1], side*(new_side[1]+1)-1])
            elif new_dir == 3:
                new_pos = np.array([side*(new_side[0]+1)-1,                       side*(new_side[1]+1)-1 - get_rel_pos(pos)[1]])
        elif dir == 2:
            if new_dir == 2:
                new_pos = np.array([side*new_side[0]       + get_rel_pos(pos)[0], side*(new_side[1]+1)-1])
            elif new_dir == 1:
                new_pos = np.array([side*new_side[0],                             side*new_side[1]       + get_rel_pos(pos)[0]])
            elif new_dir == 0:
                new_pos = np.array([side*(new_side[0]+1)-1 - get_rel_pos(pos)[0], side*new_side[1]])
            elif new_dir == 3:
                new_pos = np.array([side*(new_side[0]+1)-1,                       side*(new_side[1]+1)-1 - get_rel_pos(pos)[0]])
        elif dir == 3:
            if new_dir == 3:
                new_pos = np.array([side*(new_side[0]+1)-1,                       side*new_side[1]       + get_rel_pos(pos)[1]])
            elif new_dir == 0:
                new_pos = np.array([side*new_side[0]       + get_rel_pos(pos)[1], side*new_side[1]])
            elif new_dir == 1:
                new_pos = np.array([side*new_side[0],                             side*(new_side[1]+1)-1 -  get_rel_pos(pos)[1]])
            elif new_dir == 2:
                new_pos = np.array([side*(new_side[0]+1)-1 - get_rel_pos(pos)[1], side*(new_side[1]+1)-1])
            
        return new_pos, new_dir
    
def get_side(pos):
    index = tuple(np.array(pos) // side)
    if (0 <= index[0] < shape.shape[0]) and (0 <= index[1] < shape.shape[1]):
        return shape[index]
    else:
        return 0

def get_rel_pos(pos):
    return tuple(np.array(pos) % side)



dir = 0
print(f'starting position: {pos} in direction {moves[dir]}')

for i in path:
    if i == 'L':
        dir = (dir-1) % 4
    elif i == 'R':
        dir = (dir+1) % 4
    else:
        for _ in range(i):
            new_pos, new_dir = new(pos, dir)
            if read(new_pos) == 1:
                pos = new_pos
                dir = new_dir
                # print(f'  {new_pos} {moves[new_dir]}')
            else:
                break            
    print(f'after {i} at position: {pos} in direction {moves[dir]}')
    
print(f'final score: {1000*(pos[0]+1)+4*(pos[1]+1)+dir}')