monkeys = {}
with open('input.txt', 'r') as f:
    for line in f.readlines():
        words = line.split(':')
        monkey = words[0]
        words[1] = words[1].strip().split()
        if len(words[1]) == 1:
            # shouting number
            monkeys[monkey] = int(words[1][0])
        else:
            # shouting operation
            monkeys[monkey] = words[1]

# print(monkeys)
while type(monkeys['root']) == list:
# for _ in range(1):
    op_monkeys = 0
    for monkey in monkeys:
        if type(monkeys[monkey]) == list:
            A = monkeys[monkeys[monkey][0]]
            B = monkeys[monkeys[monkey][2]]
            # print(monkey, type(A), type(B))
            if type(A) != list and type(B) != list:
                # inputs ready!
                if monkeys[monkey][1] == '+':
                    monkeys[monkey] = A + B
                elif monkeys[monkey][1] == '-':
                    monkeys[monkey] = A - B
                elif monkeys[monkey][1] == '*':
                    monkeys[monkey] = A * B
                elif monkeys[monkey][1] == '/':
                    monkeys[monkey] = A / B
            else:
                # still operation monkey
                op_monkeys += 1
    print(f'numbers: {len(monkeys)-op_monkeys};   operations: {op_monkeys}')
    # print(monkeys)
print(monkeys['root'])