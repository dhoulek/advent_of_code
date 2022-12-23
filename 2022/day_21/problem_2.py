from tqdm import tqdm

monkeys = {}
with open('input.txt', 'r') as f:
    for line in f.readlines():
        words = line.split(':')
        monkey = words[0]
        words[1] = words[1].strip().split()
        if len(words[1]) == 1:
            # shouting number
            monkeys[monkey] = {'A': None, 'B': None, 'op': None, 'value': int(words[1][0])}
        else:
            # shouting operation
            monkeys[monkey] = {'A': words[1][0], 'B': words[1][2], 'op': words[1][1],
                               'value': None}
# ignore 'humn'
monkeys['humn']['value'] = None

# fill in all numbers shouted out
def fill_numbers():
    for m in tqdm(monkeys, desc='filling numbers'):
        for i in ['A', 'B']:
            if type(monkeys[m][i]) == str and monkeys[monkeys[m][i]]['value'] != None:
                monkeys[m][i] = monkeys[monkeys[m][i]]['value']
                
def perform_operations():
    for m in tqdm(monkeys, desc='performing operations'):
        numbers = [type(monkeys[m][X]) != str and monkeys[m][X] != None for X in ['A', 'B', 'value']]
        if sum(numbers) == 2:
            # two numbers known -> perform operations
            if numbers == [True, True, False]:
                # print(monkeys[m])
                if monkeys[m]['op'] == '+':
                    monkeys[m]['value'] = monkeys[m]['A'] + monkeys[m]['B']
                elif monkeys[m]['op'] == '-':
                    monkeys[m]['value'] = monkeys[m]['A'] - monkeys[m]['B']
                elif monkeys[m]['op'] == '*':
                    monkeys[m]['value'] = monkeys[m]['A'] * monkeys[m]['B']
                elif monkeys[m]['op'] == '/':
                    monkeys[m]['value'] = monkeys[m]['A'] / monkeys[m]['B']
            elif numbers == [True, False, True]:
                # print(monkeys[m])
                if monkeys[m]['op'] == '+':
                    monkeys[monkeys[m]['B']]['value'] =  monkeys[m]['value'] - monkeys[m]['A']
                elif monkeys[m]['op'] == '-':
                    monkeys[monkeys[m]['B']]['value'] = monkeys[m]['A'] - monkeys[m]['value']
                elif monkeys[m]['op'] == '*':
                    monkeys[monkeys[m]['B']]['value'] = monkeys[m]['value'] / monkeys[m]['A']
                elif monkeys[m]['op'] == '/':
                    monkeys[monkeys[m]['B']]['value'] = monkeys[m]['A'] / monkeys[m]['value']
            elif numbers == [False, True, True]:
                # print(monkeys[m])
                if monkeys[m]['op'] == '+':
                    monkeys[monkeys[m]['A']]['value'] =  monkeys[m]['value'] - monkeys[m]['B']
                elif monkeys[m]['op'] == '-':
                    monkeys[monkeys[m]['A']]['value'] = monkeys[m]['B'] + monkeys[m]['value']
                elif monkeys[m]['op'] == '*':
                    monkeys[monkeys[m]['A']]['value'] = monkeys[m]['value'] / monkeys[m]['B']
                elif monkeys[m]['op'] == '/':
                    monkeys[monkeys[m]['A']]['value'] = monkeys[m]['B'] * monkeys[m]['value']
            

# part 1 - getting to the 'root' operation
while type(monkeys['root']['A']) == str and type(monkeys['root']['B']) == str:
    fill_numbers()
    perform_operations()

# part 2 - perform 'root', i.e. '=' opoeration
if type(monkeys['root']['A']) == str:
    monkeys[monkeys['root']['A']]['value'] = monkeys['root']['B']
else:
    monkeys[monkeys['root']['B']]['value'] = monkeys['root']['A']
# print(monkeys['root'])
# print(monkeys)

# part 3 - resolve 'humn' value
while monkeys['humn']['value'] == None:
    fill_numbers()
    perform_operations()
print()
print(monkeys['humn'])lving