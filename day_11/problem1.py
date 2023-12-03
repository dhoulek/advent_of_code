import numpy as np

def get_flashing(field):
    flashing = []
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i,j] > 9:
                flashing.append((i, j))
    return flashing

def flash(field, i, j):
    field[i, j] = 0
    if i>0 and j>0 and field[i-1, j-1]>0:
        field[i-1, j-1] += 1
    if i>0 and field[i-1, j]>0:
        field[i-1, j] += 1
    if i>0 and j+1<field.shape[1] and field[i-1, j+1]>0:
        field[i-1, j+1] += 1
    if i+1<field.shape[0] and j>0 and field[i+1, j-1]>0:
        field[i+1, j-1] += 1
    if i+1<field.shape[0] and field[i+1, j]>0:
        field[i+1, j] += 1
    if i+1<field.shape[0] and j+1<field.shape[1] and field[i+1, j+1]>0:
        field[i+1, j+1] += 1
    if j+1<field.shape[1] and field[i, j+1]>0:
        field[i, j+1] += 1
    if j>0 and field[i, j-1]>0:
        field[i, j-1] += 1
    return field

def play_step(field):    
    field = field + np.ones(field.shape, dtype=int)

    flashing = get_flashing(field)
    while len(flashing)>0:
        for pos in flashing:
            field = flash(field, *pos)
        flashing = get_flashing(field)
    return field

def print_field(field):
    f = field.copy()
    f = f.astype('str')
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            if f[i,j] == '0':
                f[i,j] = '.'
    print(f)
    
def count_flashes(field):
    num = 0
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i,j] == 0:
                num += 1
    return num

input = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input.append([int(c) for c in line.strip()])

field = np.array(input)
print_field(field)
num_flashes = 0
for i in range(100):
    field = play_step(field)
    num_flashes += count_flashes(field)
print_field(field)

print(f'Number of flashes after 100 steps: {num_flashes}')

field = np.array(input)
num_steps = 0
while count_flashes(field)<field.size:
    field = play_step(field)
    num_steps += 1
print_field(field)

print(f'Number of steps to synchronized flashing: {num_steps}')

    