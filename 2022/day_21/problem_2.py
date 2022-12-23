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


# part 1: do until root has 1 number
M1 = monkeys['root'][0]
M2 = monkeys['root'][2]
while type(monkeys[M1]) == list and type(monkeys[M2]) == list:
    op_monkeys = 0
    for monkey in monkeys:
        # we will ignore 'human'
        if monkey != 'humn':            
            if type(monkeys[monkey]) == list:
                m1 = monkeys[monkey][0]
                A = monkeys[m1]
                m2 = monkeys[monkey][2]
                B = monkeys[m2]
                # print(monkey, type(A), type(B))
                if type(A) != list and type(B) != list and m1 != 'humn' and m2 != 'humn':
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

# fill in all known numbers
for monkey in monkeys:
    if type(monkeys[monkey]) == list:
        for i in [0, 2]:
            m = monkeys[monkey][i]
            if type(monkeys[m]) != list and m != 'humn':
                monkeys[monkey][i] = monkeys[m]
# print(monkeys)                


def inv_op(A, B, res, op):
    print(A, B, res, op)
    if type(A) == str:
        # solving A
        if op == '+':
            return res - B
        elif op == '-':
            return res + B
        elif op == '*':
            return res / B
        elif op == '/':
            return res * B
    else:
        # solving B
        if op == '+':
            return res - A
        elif op == '-':
            return A - res
        elif op == '*':
            return res / A
        elif op == '/':
            return A / res
        
# apply root operation
if type(monkeys[M1]) == list:
    res = monkeys[M2]
    solving = M1
else:
    res = monkeys[M1]
    solving = M2
    
# part 2: propagate, until we resolve 'humn'
while solving != 'humn':
    [A, op, B] = monkeys[solving]
    if type(A) == str:
        new_solving = A
        new_res = inv_op(A, B, res, op)
        print(f'{solving}: {A} {op} {B} = {res}  ==> {new_res} {op} {B} = {res}  ==> {A} = {new_res}')
    else:
        new_solving = B
        new_res = inv_op(A, B, res, op)
        print(f'{solving}: {A} {op} {B} = {res}  ==> {A} {op} {new_res} = {res}  ==> {B} = {new_res}')
    res = new_res
    solving = new_solving