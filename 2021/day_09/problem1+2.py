import numpy as np

input = []
num_lines = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input += [int(d) for d in list(line.strip())]
        num_lines += 1
line_length = len(input)//num_lines
input = np.array(input)
input = np.reshape(input, (num_lines, line_length))


minima = []
for y in range(num_lines):
    for x in range(line_length):
        loc_min = True
        if y > 0:
            loc_min = loc_min and input[y-1, x]>input[y, x]
        if y < num_lines-1:
            loc_min = loc_min and input[y+1, x]>input[y, x]
        if x > 0:
            loc_min = loc_min and input[y, x-1]>input[y, x]
        if x < line_length-1:
            loc_min = loc_min and input[y, x+1]>input[y, x]
        if loc_min:
            # print(f'minimum at [{x},{y}] with value {input[y,x ]}')
            minima.append((x, y))
risk = 0            
for x, y in minima:
    risk += 1+input[y, x]
print(f'risk value is {risk}')

def check_around(x,y):
    b = [(x, y)]
    if x>0 and input[y, x-1]>input[y, x] and input[y, x-1]!=9:
        b += check_around(x-1, y)
    if x<line_length-1 and input[y, x+1]>input[y, x] and input[y, x+1]!=9:
        b += check_around(x+1, y)
    if y>0 and input[y-1, x]>input[y, x] and input[y-1, x]!=9:
        b += check_around(x, y-1)
    if y<num_lines-1 and input[y+1, x]>input[y, x] and input[y+1, x]!=9:
        b += check_around(x, y+1)
    return b

basins = []
for x,y in minima:
    basin = set(check_around(x, y))
    basins.append(len(basin))
    # print(f'basin at [{x},{y}] has size {basins[-1]}')
    
basins = sorted(basins, reverse=True)
print(f'final answer is: {basins[0]*basins[1]*basins[2]}')