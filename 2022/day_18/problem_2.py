import pandas as pd

cubes = pd.DataFrame()
with open('test.txt', 'r') as f:
    for line in f.readlines():
        line = [int(x) for x in line.strip().split(',')]        
        cubes = pd.concat([cubes, pd.DataFrame([{'x': line[0], 'y': line[1], 'z': line[2]}])], ignore_index=True)
print(cubes)

sides = 0    
for i in cubes.index:
    x = cubes['x'][i]
    y = cubes['y'][i]
    z = cubes['z'][i]
    print(i)
    if cubes.mask((cubes['x']!=x) | (cubes['y']!=y))['z'].max() == z:
        sides += 1
    if cubes.mask((cubes['x']!=x) | (cubes['y']!=y))['z'].min() == z:
        sides += 1
    if cubes.mask((cubes['x']!=x) | (cubes['z']!=z))['y'].max() == y:
        sides += 1
    if cubes.mask((cubes['x']!=x) | (cubes['z']!=z))['y'].min() == y:
        sides += 1
    if cubes.mask((cubes['y']!=y) | (cubes['z']!=z))['x'].max() == x:
        sides += 1
    if cubes.mask((cubes['y']!=y) | (cubes['z']!=z))['x'].min() == x:
        sides += 1

print(f'free surface: {sides}')