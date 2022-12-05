pre = 'input'

with open(f'{pre}_conf.txt', 'r') as f:
    conf = f.readlines()    
conf = [list(line) for line in conf]

stacks = []
i = 1
while i<len(conf[0]):
    st = []
    for j in range(0, len(conf)):
        if conf[j][i] != ' ':
            st.append(conf[j][i])
    stacks.append(list(reversed(st[:-1])))
    i += 4

def print_stacks(stacks):
    for i, s in enumerate(stacks):
        print(f'{i+1}: '+' '.join(s))
        
print('initial configuration')
print_stacks(stacks)

with open(f'{pre}_moves.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        n = int(line[1])
        i = int(line[3])-1
        j = int(line[5])-1
        # print(n, i+1, j+1)
        stacks[j] += stacks[i][-n:]
        stacks[i] = stacks[i][:-n]

print('final configuration')
print_stacks(stacks)

print('answer: '+''.join([s[-1] for s in stacks]))