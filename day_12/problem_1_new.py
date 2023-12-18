import numpy as np
import re
from tqdm import tqdm

def find_next(pattern, after):
    for i, s in enumerate(pattern[after:]):
        if s in ['#', '?']:
            return i+start
    return None

def check(pattern, start, length):
    return ('.' not in set(pattern[start:start+length])) and (pattern[start+length] in ['.', '?'])
    
def process_line(pattern, groups):    
    free_spaces = len(pattern) - (sum(groups) + len(groups) - 1)
    options = np.zeros(len(pattern), dtype=np.int_)
    print(free_spaces, groups, len(pattern), sum(groups))
    ig = 0
    for i in range(free_spaces+1):
        options[i+groups[ig]] += check(pattern, i, groups[ig]) and ('#' not in set(pattern[:i]))
    print(pattern, ig, options, sum(groups[:ig]) + ig)
    for ig in range(1, len(groups)):
        prev = options.copy()
        options = np.zeros(len(pattern), dtype=np.int_)
        min_start = sum(groups[:ig]) + ig
        for i in range(min_start, min_start+free_spaces+1):
            used_spaces = i - min_start
            if check(pattern, i, groups[ig]):
                print('ii', i, min_start)
                options[i+groups[ig]] += sum(prev[max(0, i-min_start):i])
                if ig == len(groups)-1:
                    print('--', i, pattern, ig, options, min_start)
                    if '#' in set(pattern[i+groups[ig]:]):
                        # remaining '#' symbols after the last group!
                        options[i+groups[ig]] = 0
                    print('++', i, pattern, ig, options, min_start)
        print(pattern, ig, options, min_start)
    print(pattern, sum(options))
    return sum(options)
    


with open('input.txt', 'r') as f:
    hits = []
    # hits5 = 0
    for l in tqdm(f.readlines()[:6]):
        pattern, groups = l.strip().split()
        pattern = pattern + '.'
        groups = [int(i) for i in groups.split(',')]
        hits.append(process_line(pattern, groups))
        # hits5 += process_line('?'.join([pattern]*5), groups*5)
        # print(hits, hits5)
        
# print(hits)

old_hits = [14, 9, 1, 10, 4, 2, 5, 2, 4, 1, 4, 1, 1, 1, 3, 2, 3, 2, 6, 21, 4, 6, 21, 4, 2, 12, 4, 2, 4, 10, 6, 1, 1, 4, 2, 4, 7, 6, 40, 14, 2, 3, 9, 24, 3, 5, 2, 2, 12, 18, 3, 4, 3, 5, 28, 8, 16, 6, 6, 1, 14, 2, 1, 4, 1, 2, 1, 2, 4, 3, 8, 1, 6, 3, 2, 19, 4, 3, 1, 37, 8, 1, 3, 1, 8, 3, 6, 4, 2, 2, 9, 1, 10, 1, 2, 3, 1, 2, 6, 1, 12, 4, 2, 8, 1, 11, 10, 9, 2, 6, 2, 3, 3, 5, 1, 2, 2, 11, 6, 4, 6, 4, 3, 3, 38, 12, 65, 7, 3, 9, 10, 13, 3, 6, 1, 3, 2, 9, 9, 3, 3, 4, 1, 2, 7, 2, 6, 5, 3, 12, 3, 4, 2, 1, 1, 1, 5, 6, 1, 1, 10, 3, 7, 9, 4, 12, 11, 10, 2, 3, 3, 17, 14, 3, 7, 1, 18, 9, 9, 1, 1, 1, 15, 5, 1, 17, 1, 6, 48, 4, 6, 3, 9, 3, 4, 12, 12, 1, 4, 1, 4, 26, 1, 1, 2, 2, 8, 11, 1, 7, 10, 3, 6, 4, 2, 3, 25, 6, 10, 4, 3, 1, 4, 2, 2, 1, 5, 2, 20, 2, 2, 25, 1, 2, 2, 9, 5, 2, 6, 1, 17, 4, 16, 13, 3, 10, 4, 36, 3, 1, 1, 1, 12, 7, 10, 12, 4, 2, 4, 2, 5, 4, 4, 3, 8, 9, 3, 2, 3, 6, 2, 7, 3, 3, 3, 1, 7, 42, 4, 12, 1, 5, 1, 18, 2, 12, 18, 10, 2, 4, 11, 5, 6, 2, 3, 10, 2, 2, 1, 3, 12, 4, 2, 30, 6, 6, 56, 12, 7, 2, 8, 3, 2, 1, 1, 8, 2, 4, 7, 2, 2, 1, 4, 16, 4, 2, 5, 4, 3, 1, 1, 6, 7, 8, 3, 6, 2, 30, 30, 4, 6, 1, 3, 17, 1, 4, 3, 1, 7, 2, 24, 1, 18, 2, 9, 3, 2, 2, 22, 12, 21, 2, 3, 23, 1, 1, 10, 24, 2, 2, 3, 3, 3, 1, 8, 6, 14, 4, 4, 2, 1, 2, 6, 2, 69, 4, 13, 35, 1, 3, 7, 2, 11, 1, 1, 3, 7, 3, 1, 6, 6, 8, 4, 5, 2, 1, 3, 8, 4, 4, 4, 2, 2, 3, 2, 40, 6, 2, 4, 2, 2, 1, 5, 4, 1, 1, 5, 1, 2, 2, 28, 2, 9, 4, 80, 8, 1, 7, 7, 2, 2, 23, 5, 9, 3, 4, 3, 21, 4, 6, 3, 2, 3, 6, 2, 2, 2, 2, 7, 15, 10, 2, 6, 8, 46, 8, 1, 2, 85, 3, 4, 13, 2, 1, 18, 3, 2, 8, 3, 6, 3, 3, 1, 4, 6, 5, 2, 14, 3, 1, 4, 1, 1, 1, 2, 1, 1, 96, 29, 3, 2, 18, 1, 1, 3, 4, 45, 16, 4, 1, 6, 9, 10, 15, 4, 4, 12, 6, 3, 15, 6, 1, 4, 30, 2, 2, 8, 4, 7, 3, 7, 7, 9, 4, 6, 3, 51, 12, 1, 2, 2, 5, 3, 2, 18, 1, 1, 1, 4, 2, 2, 12, 3, 5, 1, 4, 52, 1, 7, 7, 87, 2, 9, 42, 2, 2, 2, 1, 2, 1, 56, 13, 4, 6, 4, 2, 3, 1, 1, 2, 2, 3, 2, 3, 1, 1, 4, 3, 18, 22, 3, 2, 3, 9, 7, 3, 2, 3, 4, 4, 3, 12, 24, 18, 5, 3, 3, 4, 23, 2, 3, 3, 10, 16, 1, 2, 21, 13, 1, 10, 6, 4, 43, 45, 5, 1, 6, 4, 7, 14, 3, 1, 1, 5, 4, 6, 8, 2, 18, 9, 12, 10, 8, 2, 10, 9, 4, 2, 66, 8, 4, 4, 1, 2, 1, 22, 5, 1, 3, 17, 48, 4, 6, 6, 6, 4, 19, 30, 2, 2, 10, 5, 5, 12, 2, 3, 4, 9, 10, 6, 1, 6, 4, 7, 19, 3, 3, 8, 12, 4, 16, 13, 11, 1, 6, 6, 8, 8, 1, 1, 6, 11, 126, 3, 2, 3, 1, 3, 2, 4, 7, 2, 4, 7, 6, 8, 2, 1, 1, 11, 1, 12, 2, 1, 9, 4, 1, 2, 4, 4, 22, 1, 5, 12, 7, 4, 8, 2, 2, 2, 3, 2, 10, 2, 1, 18, 3, 1, 1, 3, 6, 2, 1, 3, 4, 1, 4, 11, 3, 3, 2, 3, 3, 3, 3, 10, 18, 4, 8, 6, 1, 4, 4, 1, 9, 2, 9, 12, 6, 1, 1, 6, 6, 4, 2, 6, 2, 10, 4, 8, 7, 3, 3, 16, 2, 6, 2, 1, 4, 2, 9, 4, 1, 62, 10, 4, 3, 8, 2, 3, 120, 9, 12, 13, 3, 2, 4, 6, 3, 3, 6, 2, 4, 15, 8, 43, 6, 4, 34, 6, 20, 14, 2, 2, 1, 2, 4, 1, 2, 1, 1, 3, 1, 2, 1, 2, 29, 10, 3, 1, 3, 18, 15, 4, 1, 4, 6, 2, 3, 3, 4, 4, 6, 18, 11, 1, 10, 3, 1, 1, 3, 1, 6, 6, 6, 6, 2, 9, 4, 2, 1, 1, 9, 6, 5, 22, 1, 4, 2, 2, 10, 9, 17, 2, 4, 3, 1, 9, 6, 9, 21, 2, 1, 2, 2, 4, 54, 6, 3, 4, 1, 1, 8, 1, 1, 1, 1, 3, 1, 6, 2, 2, 12, 3, 1, 2, 2, 3, 9, 6, 7, 4, 12, 2, 2, 17, 6, 4, 2, 42, 6, 2, 2, 2, 1, 4, 21, 1, 3, 6, 9, 8, 1, 24, 3, 10, 3, 1, 4, 7, 3, 2, 22, 7, 2, 1, 21, 1, 6, 94, 8, 1, 5, 2, 14, 3, 2, 7, 6, 6, 2, 16, 2, 2, 1, 6, 17, 1, 2, 1, 4, 60, 2, 3, 2, 17, 1, 2, 6, 2]

print(len(old_hits), len(hits))
for i in range(len(hits)):
    if old_hits[i] != hits[i]:
        print(i, old_hits[i], hits[i])
        break

        
print('Part 1:')
print(f'Sum of possible arrangements: {sum(hits)}\n')