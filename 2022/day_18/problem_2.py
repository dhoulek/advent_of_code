from itertools import product

cubes = set()

xmax = -100000
ymax = -100000
zmax = -100000
xmin = 100000
ymin = 100000
zmin = 100000
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = tuple(int(x) for x in line.strip().split(','))
        cubes.add(line)
        xmax = max(xmax, line[0])
        ymax = max(ymax, line[1])
        zmax = max(zmax, line[2])
        xmin = min(xmin, line[0])
        ymin = min(ymin, line[1])
        zmin = min(zmin, line[2])
print(f'({xmin}:{xmax}) x ({ymin}:{ymax}) x ({zmin}:{zmax})')
# expanding the playground a bit
xmin -= 2
xmax += 1
ymin -= 1
ymax += 1
zmin -= 1
zmax += 1

# inverse casting  
form = set([(xmin, ymin, zmin)])
to_process = form.copy()
while len(to_process) > 0:
    (x, y, z) = to_process.pop()
    for (i, j, k) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
                      (0, 0, 1), (0, 0, -1)]:
        if (xmin <= x+i <= xmax) and (ymin <= y+j <=ymax) and (zmin <= z+k <= zmax):
            if (x+i, y+j, z+k) not in cubes:
                if (x+i, y+j, z+k) not in form:
                    to_process.add((x+i, y+j, z+k))
                    form.add((x+i, y+j, z+k))

# fill the wholes - add all what it not in the form
for x, y, z in product(range(xmin, xmax+1), range(ymin, ymax+1), range(zmin, zmax+1)):
    if (x, y, z) not in form:
        cubes.add((x, y, z))
            
# now we have a solid object without pores -- apply solution of problem 1
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