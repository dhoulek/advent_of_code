import numpy as np

paths = []
min_x = 10000
max_x = -10000
min_y = 0
max_y = -10000
with open('input.txt', 'r') as f:    
    for line in f.readlines():
        path = []
        for point in line.strip().split('->'):
            path.append([int(x) for x in point.strip().split(',')])
            min_x = min((min_x, path[-1][0]))
            max_x = max((max_x, path[-1][0]))
            min_y = min((min_y, path[-1][1]))
            max_y = max((max_y, path[-1][1]))
        paths.append(path)

# increase dimensions for the "infinite" bottom size
max_y += 2
min_x -= 1000
max_x += 1000
print(f'Cave dimensions: ({min_x}..{max_x})x({min_y}..{max_y})')
paths.append([[min_x, max_y], [max_x, max_y]])
# generate cave
origin = (min_x, min_y)
cave = np.zeros(((max_x-min_x+1), (max_y-min_y+1)), dtype=np.int)
for path in paths:
    for p1, p2 in zip(path[:-1], path[1:]):
        # print(p1, p2)
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
            for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                # print(x, y)
                cave[x-origin[0]][y-origin[1]] = 1
# source of sand
source = (500-origin[0], 0-origin[1])
cave[source] = 2
print(cave.T)

def sand_unit():
    pos = np.array(source)
    rest = False
    infinity = False
    while not rest and not infinity:        
        if not ((min_x <= pos[0]+origin[0] <= max_x)
                and (min_y <= pos[1]+origin[1] <= max_y)):
            infinity = True
        else:
            if cave[pos[0], pos[1]+1] == 0:
                # fall down
                pos = pos + (0,1)
            elif pos[0] == 0:
                # fall to inifinity on left
                infinity = True
            elif cave[pos[0]-1, pos[1]+1] == 0:
                # fall diagonally to left
                pos = pos + (-1,1)
            elif pos[0] == max_x-origin[0]:
                # fall to inifinity on right
                infinity = True
            elif cave[pos[0]+1, pos[1]+1] == 0:
                # fall diagonally to right
                pos = pos + (1,1)
            else:
                cave[tuple(pos)] = 3
                rest = True
        
        # print(rest, infinity, min_x, pos[0]+origin[0], max_x, min_y, pos[1]+origin[1], max_y)
    return pos
    
units = 0
pos = origin
while abs(pos[0]-source[0])+abs(pos[1]-source[1]) > 0:
    pos = sand_unit()
    units += 1
    print('unit:', units)
print(cave.T)