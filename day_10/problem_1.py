collect = {i: None for i in range(20, 230, 40)}

cycle = 0
signal = 1
display = ''


def perform_cycle(value):
    global cycle
    global signal
    cycle += 1
    if cycle in collect.keys():
        collect[cycle] = signal
    signal += value
    # print(cycle, signal, collect)

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        if line[0] == 'noop':
            perform_cycle(0)
        elif line[0] == 'addx':
            perform_cycle(0)
            perform_cycle(int(line[1]))

strength = sum([collect[i]*i for i in collect.keys()])
print('sum of signal strengths is', strength)
        
    