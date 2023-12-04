import numpy as np

# Function to find the next numeric entry in the input grid
def find_next_number(x, y):
    while not input[y, x].isnumeric():
        x += 1
        if x > size:
            x = 1
            y += 1
        if y > size:
            return None
    n = ''
    while x <= size and input[y, x].isnumeric():
        n += input[y, x]
        x += 1
    return (n, x, y)

# Function to check if there are symbols around a given number
def check_symbol_around(x, y, l):
    # Extract the frame around the current position
    frame = list(input[y-1, x-1:x+l+1])  # above
    frame += list(input[y+1, x-1:x+l+1])  # below
    frame += [input[y, x-1], input[y, x+l]]  # left and right
    symbols = [c for c in frame if not c.isnumeric() and c != '.']
    return len(symbols) > 0

# Function to check and record stars around a given position
def check_stars(x, y, n):
    l = len(n)
    frame = [(xx, y-1) for xx in range(x-1, x+l+1)]  # above
    frame += [(xx, y+1) for xx in range(x-1, x+l+1)]  # below
    frame += [(x-1, y), (x+l, y)]  # left and right
    for pos in frame:
        if pos in stars.keys():
            stars[pos].append(int(n))

# Read input from a file  containing the grid with  numbers and 
# symbols. We additionally decorate all inputs with '.' around 
# it, so that later we don't need to check so carefully the 
# limits - every number will be _fully_ surrounded by some entries.
input = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        input.append(np.array(['.'] + list(line.strip()) + ['.']))
top = ['.' for _ in range(len(input[0]))]
input = np.array([top] + input + [top])

# Adjust the size for later use in the loop
size, _ = input.shape
size -= 2

# Prepare for Part 2: dictionary with keys being positions of 
# the stars and values being lists of the surrounding part numbers
stars = {}
for x in range(1, size+1):
    for y in range(1, size+1):
        if input[y, x] == '*':
            stars[(x, y)] = []

part_numbers = []

# Start from the top-left corner
x, y = (1, 1)
num = find_next_number(x, y)

# Loop to find and process all numeric entries in the grid
while (num is not None) and (y <= size):
    n, x, y = num
    l = len(n)
    if check_symbol_around(x-l, y, l):
        part_numbers.append(int(n))
        check_stars(x-l, y, n)
    num = find_next_number(x, y)

# Print results for Part 1
print('Part 1')
print(f'Sum of part numbers is {sum(part_numbers)}\n')

# Calculate and print results for Part 2
gear_ratios_sum = 0
for gears in stars.values():
    if len(gears) == 2:
        gear_ratios_sum += np.prod(gears)

print('Part 2')
print(f'Sum of all gear ratios is {gear_ratios_sum}')