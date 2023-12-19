# Algorithm inspired frrom
# https://github.com/maneatingape/advent-of-code-rust/blob/main/src/year2023/day12.rs

# Import necessary libraries
import numpy as np
from tqdm import tqdm

# Function to check if a pattern can be placed at a specific position in the sequence
def check(pattern, start, length):
    return ('.' not in set(pattern[start:start+length])) and (pattern[start+length] in ['.', '?'])

# Function to process a single line of the input and calculate possible arrangements
def process_line(pattern, groups):    
    # Calculate the number of free spaces in the pattern
    free_spaces = len(pattern) - (sum(groups) + len(groups) - 1)
    # Initialize an array to store options for placing groups
    options = np.zeros(len(pattern), dtype=np.int_)
    
    if verbose:
        print(free_spaces, groups, len(pattern), sum(groups))
    
    # Process the first group
    ig = 0
    for i in range(free_spaces+1):
        options[i+groups[ig]] += check(pattern, i, groups[ig]) and ('#' not in set(pattern[:i]))
    
    if verbose:
        print()
        print(np.array([i//10 for i in range(len(pattern))]))
        print(np.array([i%10 for i in range(len(pattern))]))
        print(' ' + ' '.join(list(pattern)))
        print(options)
    
    # Process the remaining groups
    for ig in range(1, len(groups)):
        prev = options.copy()
        options = np.zeros(len(pattern), dtype=np.int_)
        min_start = sum(groups[:ig]) + ig - 1
        if verbose:
            print(ig, min_start)
        for i in range(min_start, min_start+free_spaces+1):
            used_spaces = i - min_start
            if check(pattern, i, groups[ig]):
                # Add only if no '#' symbol between previous and this group
                options[i+groups[ig]] += sum([prev[ip] for ip in range(min_start, i) if '#' not in set(pattern[ip:i])])
                
                # Special treatment of the last group
                if ig == len(groups)-1:
                    if '#' in set(pattern[i+groups[ig]:]):
                        # Remaining '#' symbols after the last group!
                        options[i+groups[ig]] = 0
        if verbose:
            print(options)
    
    if verbose:
        print(pattern, sum(options))
        print('')
    
    # Return the total number of possible arrangements for the line
    return sum(options)

# Set verbosity flag (for debugging purposes)
verbose = False

# Read input from a file
with open('input.txt', 'r') as f:
    hits = []
    hits5 = []
    # Iterate over each line in the input file
    for l in tqdm(f.readlines()[:]):
        # Parse the line into pattern and groups
        pattern, groups = l.strip().split()
        groups = [int(i) for i in groups.split(',')]
        # Calculate and store the number of possible arrangements for the line
        hits.append(process_line(pattern + '.', groups))
        # Calculate and store the number of possible arrangements for the line repeated five times
        hits5.append(process_line('?'.join([pattern]*5) + '.', groups*5))
             
# Print results for Part 1
print('Part 1:')
print(f'Sum of possible arrangements: {sum(hits)}\n')

# Print results for Part 2
print('Part 2:')
print(f'Sum of unfolded arrangements: {sum(hits5)}')
