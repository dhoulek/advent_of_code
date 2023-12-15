import numpy as np

# Read input file and create a padded 2D array representing the field
field = []
with open('input.txt', 'r') as f:
    for l in f.readlines():
        field.append(['.'] + list(l.strip()) + ['.'])

field = np.array([['.']*len(field[0])] + field + [['.']*len(field[0])])

# Locate the start position and its neighbors
[y], [x] = np.where(field == 'S')
S = np.array([y, x])
n, e, s, w = [field[y-1, x], field[y, x+1], field[y+1, x], field[y, x-1]]
n_in = ['|', 'F', '7']
s_in = ['|', 'J', 'L']
e_in = ['J', '-', '7']
w_in = ['L', '-', 'F']

# Determine the symbol at the start position based on its neighbors
if n in n_in and s in s_in:
    Ssymb = '|'
elif n in n_in and e in e_in:
    Ssymb = 'L'
elif n in n_in and w in w_in:
    Ssymb = 'J'
elif w in w_in and e in e_in:
    Ssymb = '-'
elif w in w_in and s in s_in:
    Ssymb = '7'
else:
    Ssymb = 'F'
field[y, x] = Ssymb

# Define the clockwise order of neighbors and the corresponding options for each symbol
# Indexing is anti-clockwise
neigh = [np.array([-1, 0]), np.array([0, -1]), np.array([1, 0]), np.array([0, 1])]
options = [['F', '|', '7'], ['F', '-', 'L'], ['L', '|', 'J'], ['J', '-', '7']]
allowed = {
    'F': [[] ,[], options[2], options[3]],
    '|': [options[0], [], options[2], []],
    '7': [[], options[1], options[2], []],
    'J': [options[0], options[1], [], []],
    'L': [options[0], [], [], options[3]],
    '-': [[], options[1], [], options[3]],
}

# Function to find the next position and direction
def find_next(curr, last):
    y, x = curr
    for i in range(4):
        ynew, xnew = curr + neigh[i]
        if i != (last+2) % 4 and field[ynew, xnew] in allowed[field[y, x]][i]:
            return curr + neigh[i], i

# Traverse the loop to find the farthest point from the starting position
loop = [S]
curr, dir = find_next(S, 0) 
while not (curr == S).all():
    loop.append(curr)
    curr, dir = find_next(curr, dir)

# Output Part 1 result
print('Part 1:')
print(f'Number of steps along the loop to the point farthest from the starting position: {len(loop)//2}\n')

# Define sets of states to keep or reverse, and count state transitions
others_keep_state = ['L7', 'FJ']
others_reverse_state = ['LJ', 'F7']
count = ['7F', '7L', '7|', 'JF', 'JL', 'J|', '|L', '|F', '||']
allowed = others_keep_state + others_reverse_state + count

# Count the number of inside tiles using the loop and symbol transitions
points = {}
for (y, x) in loop:
    if field[y, x] != '-':
        if y in points.keys():
            points[y].append(x)
        else:
            points[y] = [x]

inside = 0
for y in sorted(points.keys()):
    out = True
    p = sorted(points[y])
    for x1, x2 in zip(p[:-1], p[1:]):
        s1 = field[y, x1]
        s2 = field[y, x2]
        
        # Test if we captured all cases; this should get NEVER evaluated
        if s1+s2 not in allowed:
            print(y, x1, x2, s1, s2)
            
        if s1+s2 in count:
            if out:
                # This segment is inside
                inside += x2 - (x1+1)                
            # Change "state"
            out = not out
        elif s1+s2 in others_reverse_state:
            # We hit a part where we need to reverse the state
            out = not out

# Output Part 2 result
print('Part 2:')
print(f'Number of inside tiles: {inside}')