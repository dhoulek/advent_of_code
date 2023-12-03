from tqdm import tqdm

with open('input.txt', 'r') as f:
    molecule = f.readline().strip()
    f.readline()
    rules = {}
    for line in f.readlines():
        rules[line.split()[0]] = line.strip().split()[-1]
        
print(f'initial molecule has {len(molecule)} letters')
print(f'{len(rules)} rules gives')

def make_step(molecule):
    m = molecule[0]
    for i in range(1, len(molecule)):
        pair = ''.join(molecule[i-1:i+1])
        if pair in rules.keys():
            m += rules[pair]
        m += molecule[i]
    return m
        
for i in tqdm(range(10)):
    molecule = make_step(molecule)

letters = set(list(molecule))
count = {c: 0 for c in letters}
for c in molecule:
    count[c] += 1
    
min_val = min(count.values())
max_val = max(count.values())

print(f'max - min = {max_val-min_val}')
