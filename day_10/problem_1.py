import numpy as np

field = []
with open('test3.txt', 'r') as f:
# with open('input.txt', 'r') as f:
    for l in f.readlines():
        field.append(['.']+list(l.strip())+['.'])

field = np.array([['.']*len(field[0])] + field + [['.']*len(field[0])])
print(field)

# look up start position
[x], [y] = np.where(field == 'S')
S = np.array([x, y])
print(S)

#  indexing ANTIclockwise
#        above              left               below             right
neigh = [np.array([-1, 0]), np.array([0, -1]), np.array([1, 0]), np.array([0, 1])]
options = [['F', '|', '7' ,'S'], ['F', '-', 'L', 'S'], ['L', '|', 'J', 'S'], ['J', '-' , '7', 'S']]
allowed = {
    'S': options,
    'F': [[] ,[], options[2], options[3]],
    '|': [options[0], [], options[2], []],
    '7': [[], options[1], options[2], []],
    'J': [options[0], options[1], [], []],
    'L': [options[0], [], [], options[3]],
    '-': [[], options[1], [], options[3]],
}

def find_next(curr, last):
    for i in range(4):
        if i != (last+2)%4 and field[*(curr+neigh[i])] in allowed[field[*curr]][i]:
            return curr+neigh[i], i

loop = [S]
curr, dir = find_next(S, 0) 
while not (curr == S).all():
    loop.append(curr)
    # print(curr, field[*curr], dir)
    # for x in range(curr[0]-1, curr[0]+2):
    #     print(' '.join(field[x, curr[1]-1:curr[1]+2]))
    curr, dir = find_next(curr, dir)

print('Part 1:')
print(f'Number of steps along the loop to the point farthest from the starting position: {len(loop)//2}\n')

points = {}
for (y, x) in loop:
    if y in points.keys():
        points[y].append(x)
    else:
        points[y] = [x]
inside = 0
for y in sorted(points.keys()):
    out = True
    print(y, sorted(points[y]))
    for x in sorted(points[y]):
        if out:
            out = False
            xstart = x
            print(x, field[y, x])
        else:
            if field[y, x] == '-':
                xstart = x
            elif field[y, x] in ['7', 'J']:
                out = True
            else:
                inside += x - (xstart+1)
                out = True
    print(inside)
print(inside)