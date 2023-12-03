x = 0
y = 0
aim = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        c, v = line.split()[:2]
        v = int(v)
        if c[0] == 'f':
            x += v
            y += aim*v
        elif c[0] == 'u':
            aim -= v
        elif c[0] == 'd':
            aim += v
        else:
            print('I don\'t understand')

print(f'final coordinates: x={x}, y={y}')
print(f'answer = {x*y}')