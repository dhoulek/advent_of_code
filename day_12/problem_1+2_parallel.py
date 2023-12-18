import numpy as np
import re
from tqdm import tqdm
from multiprocessing import Pool

def process(pattern, groups):
    # print(' ', pattern, groups)
    if len(groups) == 0:
        if re.match(pattern, 'o'*len(pattern)):
            # print('  FOUND 1')
            return 1
        else:
            return 0
    else:
        options = 0
        free_spaces = len(pattern) - (sum(groups) + len(groups) - 1)
        g = groups[0]
        # print('_  ', free_spaces, g, groups)
        if len(groups[1:]) > 0:
            sep = 'o'
        else:
            sep = ''
        for i in range(free_spaces+1):
            s = 'o'*i+'#'*g+sep
            ls = len(s)
            # print(f'   _{i}_', s, pattern[:ls], re.match(pattern[:ls], s))
            if re.match(pattern[:ls], s):
                options += process(pattern[ls:], groups[1:])
            # else:
                # print('    ', s, pattern[:ls], 'STOP')
        return options


def process_line(l):
    pattern, groups = l.strip().split()
    pattern = pattern.replace('.', 'o').replace('?', '.') # python regex compatible
    groups = [int(i) for i in groups.split(',')]
    return process('.'.join([pattern]*5), groups*5)
    
filename = 'input.txt'
with open(filename, 'r') as f:
    hits = 0
    for l in tqdm(f.readlines()):
        pattern, groups = l.strip().split()
        pattern = pattern.replace('.', 'o').replace('?', '.') # python regex compatible
        groups = [int(i) for i in groups.split(',')]
        hits += process(pattern, groups)        
        
print('Part 1:')
print(f'Sum of possible arrangements: {hits}\n')

with open(filename, 'r') as f:
    lines = f.readlines()
    
pool = Pool()
hits5 = []
for result in tqdm(pool.imap_unordered(process_line, lines), total=len(lines)):
    hits5.append(result)
     
print('Part 2:')
print(f'Sum of unfolded arrangements: {sum(hits5)}')