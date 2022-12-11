from math import floor

monkey = {
    'items': [],
    'op': '',
    'value': 0,
    'condition': None,
    'true': 0,
    'false': 0
    }

monkeys = {}

with open('input.txt', 'r') as f:
    m = monkey.copy()
    for line in f.readlines():
        line = line.strip().split()
        if line == []:
            monkeys[i_monkey] = m
            m = monkey.copy()
        else:
            if line[0] == "Monkey":
                i_monkey = int(line[1][:-1])
            elif line[0] == "Starting":
                m['items'] = [int(i.split(',')[0]) for i in line[2:]]
            elif line[0] == "Operation:":
                m['op'] = line[4]
                if line[5] == 'old':
                    m['op'] = '**'
                else:
                    m['value'] = int(line[5])
            elif line[0] == "Test:":
                m['condition'] = int(line[3])
            elif line[0] == "If":
                # print(line)
                m[line[1][:-1]] = int(line[5])
    monkeys[i_monkey] = m
activity = [0]*len(monkeys)

# get a common multiple of all divisors
# we will keep only modulos w.r.t. to this common divisors of all worry
# levels, in order to prevet overflows
com = 1
for im in monkeys.keys():
    com *= monkeys[im]['condition']

def play_monkey(im):
    items = monkeys[im]['items']
    monkeys[im]['items'] = []
    activity[im] += len(items)
    # playing the all items of monkey im
    for level in items:        
        # increase level
        if monkeys[im]['op'] == '+':
            level += monkeys[im]['value']
        elif monkeys[im]['op'] == '*':
            level *= monkeys[im]['value']
        elif monkeys[im]['op'] == '**':
            level = level**2
        # now there is no relief but we need to prevent
        # overflow of the integers
        level = level % com
        # test
        cond = level % monkeys[im]['condition'] == 0
        if cond:
            new_monkey = monkeys[im]['true']
        else:
            new_monkey = monkeys[im]['false']
        # add it to the new_monkey
        monkeys[new_monkey]['items'] = monkeys[new_monkey]['items']+[level]
        # print(monkeys)

def print_monkeys():
    for im in monkeys.keys():
        print(f" Monkey {im}: {monkeys[im]['items']}")
    print(f" Inspection activity: {activity}")


print_monkeys()        
for r in range(10000):
    # play one round
    for im in monkeys.keys():
        play_monkey(im)    
    if (r+1) % 1000 == 0:
        print(f'\nAfter round {r+1}:')
        print_monkeys()
    
activity = list(reversed(sorted(activity)))
print(f"\nMonkey business: {activity[0]*activity[1]}")