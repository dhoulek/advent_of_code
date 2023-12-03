cubes = set()
with open('input.txt', 'r') as f:
    for line in f.readlines():
        cubes.add(tuple(int(x) for x in line.strip().split(',')))

sides = 0    
for (x, y, z) in cubes:
    if (x+1, y, z) not in cubes:
        sides += 1
    if (x-1, y, z) not in cubes:
        sides += 1
    if (x, y+1, z) not in cubes:
        sides += 1
    if (x, y-1, z) not in cubes:
        sides += 1
    if (x, y, z+1) not in cubes:
        sides += 1
    if (x, y, z-1) not in cubes:
        sides += 1

print(f'free surface: {sides}')