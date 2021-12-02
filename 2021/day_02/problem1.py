x = 0
y = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        c, v = line.split()[:2]
        v = int(v)
        if c[0] == 'f':
            x += v
        elif c[0] == 'u':
            y -= v
        elif c[0] == 'd':
            y += v
        else:
            print('I don\'t understand')

print(f'final coordinates: x={x}, y={y}')
print(f'answer = {x*y}')