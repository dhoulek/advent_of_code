blizz = []
orient = []
dirs = ['>', 'v', '<', '^']
maxx = 0
maxy = 0
with open('input.txt', 'r') as f:
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            if c in dirs:
                blizz.append(tuple([x-1, y-1]))
                orient.append(dirs.index(c))
    maxy = y-1
    maxx = x-1
final = tuple([maxx-1, maxy-1])
initial = tuple([0, 0])

def next_blizz_step():
    for i, b in enumerate(blizz):
        if orient[i] == 0:
            blizz[i] = tuple([(b[0]+1) % maxx, b[1]])
        elif orient[i] == 1:
            blizz[i] = tuple([b[0], (b[1]+1) % maxy])
        elif orient[i] == 2:
            blizz[i] = tuple([(b[0]-1) % maxx, b[1]])
        elif orient[i] == 3:
            blizz[i] = tuple([b[0], (b[1]-1) % maxy])
            
def next_positions():
    global pos
    new_pos = []
    for p in pos:
        if p not in blizz:
            new_pos.append(p)
        if p[1]>=0 and p[0]>0 and tuple([p[0]-1, p[1]]) not in blizz:
            new_pos.append(tuple([p[0]-1, p[1]]))
        if p[1]>=0 and p[0]<maxx-1 and tuple([p[0]+1, p[1]]) not in blizz:
            new_pos.append(tuple([p[0]+1, p[1]]))
        if p[1]>0 and tuple([p[0], p[1]-1]) not in blizz:
            new_pos.append(tuple([p[0], p[1]-1]))
        if p[1]<maxy-1 and tuple([p[0], p[1]+1]) not in blizz:
            new_pos.append(tuple([p[0], p[1]+1]))
    pos = set(new_pos)
    
def next_positions_back():
    global pos
    new_pos = []
    for p in pos:
        if p not in blizz:
            new_pos.append(p)
        if p[1]<maxy and p[0]>0 and tuple([p[0]-1, p[1]]) not in blizz:
            new_pos.append(tuple([p[0]-1, p[1]]))
        if p[1]<maxy and p[0]<maxx-1 and tuple([p[0]+1, p[1]]) not in blizz:
            new_pos.append(tuple([p[0]+1, p[1]]))
        if p[1]>0 and tuple([p[0], p[1]-1]) not in blizz:
            new_pos.append(tuple([p[0], p[1]-1]))
        if p[1]<maxy-1 and tuple([p[0], p[1]+1]) not in blizz:
            new_pos.append(tuple([p[0], p[1]+1]))
    pos = set(new_pos)
        
area = (maxx+1)*(maxy+1)
step = 0

pos = set([tuple([0,-1])])
while final not in pos:
    step += 1
    next_blizz_step()
    next_positions()
    print(f'time: {step}, empty tiles: {area-len(set(blizz))}, reachable tiles: {len(pos)}')
next_blizz_step()
step += 1
goal = step
print(f'First time reached destinattion after {goal} minutes')

pos = set([tuple([maxx-1, maxy])])
while initial not in pos:
    step += 1
    next_blizz_step()
    next_positions_back()
    print(f'time: {step}, empty tiles: {area-len(set(blizz))}, reachable tiles: {len(pos)}')
next_blizz_step()
step += 1
back = step
print(f'Back at origin after {back} minutes')

pos = set([tuple([0,-1])])
while final not in pos:
    step += 1
    next_blizz_step()
    next_positions()
    print(f'time: {step}, empty tiles: {area-len(set(blizz))}, reachable tiles: {len(pos)}')
step += 1
print(f'Finally again at the destination after {step} minutes')

print('\n----- SUMMARY -----')
print(f'First time reached destinattion after {goal} minutes')
print(f'Back at origin after {back} minutes')
print(f'Finally again at the destination after {step} minutes')
