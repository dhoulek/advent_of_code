from itertools import product
from tqdm import tqdm

cubes = set()

ax_x = []
ax_y = []
ax_z = []


with open('input2.txt', 'r') as f:
    input = f.readlines()

for line in input:
    command, coords = line.split(' ')
    coords = [int(l.split('=')[-1]) for x in coords.split(',') for l in x.split('..')]
    ax_x += [coords[0], coords[1]+1]
    ax_y += [coords[2], coords[3]+1]
    ax_z += [coords[4], coords[5]+1]
        
# print('ax_y:', sorted(ax_y))

ax_x = sorted(list(set(ax_x)))
ax_y = sorted(list(set(ax_y)))
ax_z = sorted(list(set(ax_z)))

# print('ax_x:', ax_x)
# print('ax_z:', ax_z)

print('lengths of axes:', len(ax_x), len(ax_y), len(ax_z))

cubes = set()

print('processing input:')
for line in tqdm(input):
    command, coords = line.split(' ')
    # print(line.strip())
    coords = [int(l.split('=')[-1]) for x in coords.split(',') for l in x.split('..')]
    coords[0] = ax_x.index(coords[0])
    coords[1] = ax_x.index(coords[1]+1)
    coords[2] = ax_y.index(coords[2])
    coords[3] = ax_y.index(coords[3]+1)
    coords[4] = ax_z.index(coords[4])
    coords[5] = ax_z.index(coords[5]+1)
    if command == 'on':
        for x, y, z in product(range(coords[0], coords[1]), range(coords[2], coords[3]),
                                range(coords[4], coords[5])):                
            l = f'{x}_{y}_{z}'
            cubes.add(l)
    elif command == 'off':
        for x, y, z in product(range(coords[0], coords[1]), range(coords[2], coords[3]),
                            range(coords[4], coords[5])):                
            l = f'{x}_{y}_{z}'
            cubes.discard(l)
print(f'number of representative regions: {len(cubes)}')

print('getting volume')
vol = 0
for l in tqdm(cubes):
    x, y, z = l.split('_')
    x = int(x)
    y = int(y)
    z = int(z)
    vol += (ax_x[x+1]-ax_x[x])*(ax_y[y+1]-ax_y[y])*(ax_z[z+1]-ax_z[z])   
print(f'number of cubes in the "on" state: {vol}')