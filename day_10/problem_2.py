cycle = 0
signal = 1
display = ''


def perform_cycle(value):
    global cycle
    global signal
    global display
    # pixel posision
    pixel = cycle % 40
    # check if sprite overlaps with pixel
    if abs(signal-pixel) <= 1:
        display += '#'
    else:
        display += '.'
    cycle += 1
    # print line if at the edn
    if pixel == 39:
        print(display)
        display = ''
    signal += value

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        if line[0] == 'noop':
            perform_cycle(0)
        elif line[0] == 'addx':
            perform_cycle(0)
            perform_cycle(int(line[1]))