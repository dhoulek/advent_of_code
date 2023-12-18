import numpy as np
import re
from tqdm import tqdm

def generate_options(N, DoF):
    if N > 1:
        cases = []
        for i in range(DoF+1):
            rest = generate_options(N-1, DoF-i)
            for c in rest:
                cases.append([i]+c)
    else:
        cases = [[DoF]]
    return cases

def check(pattern, str):
    for p, s in zip(pattern, str):
        if p != '?' and p != s:
            return False
    return True

def process_line(pattern, groups):    
    free_spaces = len(pattern) - (sum(groups) + len(groups) - 1)
    # print(pattern, groups, free_spaces)
    p = re.compile(pattern.replace('?', '.'))
    sep = np.array([0] + [1]*(len(groups)-1) + [0])
    options = generate_options(len(groups)+1, free_spaces)
    # print(len(options))
    hits = 0
    for o in options:
        o = np.array(o) + sep
        s = 'o'*o[0]
        for g, e in zip(groups, o[1:]):
            s += '#'*g + 'o'*e
        if p.match(s):
            hits += 1
    return hits



with open('input.txt', 'r') as f:
    hits = []
    for l in tqdm(f.readlines()):
        pattern, groups = l.strip().split()
        pattern = pattern.replace('.', 'o')
        groups = [int(i) for i in groups.split(',')]
        hits.append(process_line(pattern, groups))
print(hits)
        
print('Part 1:')
print(f'Sum of possible arrangements: {sum(hits)}\n')