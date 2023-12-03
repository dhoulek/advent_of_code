from os import POSIX_FADV_DONTNEED
from tqdm import tqdm

with open('input.txt', 'r') as f:
    molecule = f.readline().strip()
    f.readline()
    rules = {}
    for line in f.readlines():
        rules[line.split()[0]] = line.strip().split()[-1]
        
print(f'initial molecule has {len(molecule)} letters')
print(f'{len(rules)} rules gives')

letters = ''.join(set(molecule+''.join(rules.values())))
all_pairs = []
for c in letters:
    for d in letters:
        all_pairs.append(c+d)
print(all_pairs)        
pairs = {p: 0 for p in all_pairs}
for i in range(len(molecule)-1):
    pairs[molecule[i:i+2]] += 1

def make_step(pairs):
    new_pairs = {p: 0 for p in all_pairs}
    for pair in pairs:        
        if pair in rules.keys():
            m = rules[pair]
            p1 = pair[0]+m
            p2 = m+pair[1]
            new_pairs[p1] += pairs[pair]
            new_pairs[p2] += pairs[pair]
        else:
            new_pairs[pair] += pairs[pair]
    return new_pairs
        
for i in tqdm(range(40)):
    pairs = make_step(pairs)
    
print(pairs)

count = {c: 0 for c in letters}
for pair in pairs.keys():
    count[pair[0]] += pairs[pair]/2
    count[pair[1]] += pairs[pair]/2
count[molecule[0]] += 0.5
count[molecule[-1]] += 0.5
print(count)
    
min_val = min(count.values())
max_val = max(count.values())

print(f'max - min = {int(max_val-min_val)}')
