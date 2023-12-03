from itertools import product

cubes = set()

with open('input1.txt', 'r') as f:
    for line in f:
        print(line.strip())
                
        command, coords = line.split(' ')
        coords = [int(l.split('=')[-1]) for x in coords.split(',') for l in x.split('..')]
        if command == 'on':
            for x, y, z in product(range(coords[0], coords[1]+1), range(coords[2], coords[3]+1),
                                   range(coords[4], coords[5]+1)):                
                l = f'{x}_{y}_{z}'
                cubes.add(l)
        elif command == 'off':
               for x, y, z in product(range(coords[0], coords[1]+1), range(coords[2], coords[3]+1),
                                   range(coords[4], coords[5]+1)):                
                l = f'{x}_{y}_{z}'
                cubes.discard(l)
print(len(cubes))