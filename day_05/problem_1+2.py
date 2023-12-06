import pandas as pd

# List to store mappings
mappings = []

# Opening the input file for reading
# Change the file name to 'test.txt' if needed for testing
with open('input.txt', 'r') as f:
    # Reading seeds from the first line
    seeds = [int(i) for i in f.readline().strip().split(':')[-1].split()]

    # Reading recipes
    mapping = []
    for l in f.readlines():
        if l.strip() == '':
            # End of a mapping section; add the mapping to the list
            if len(mapping) > 0:
                mappings.append(pd.DataFrame(mapping).sort_values(by='src_first'))
            mapping = []
        elif l.strip()[-1] == ':':
            # Skip lines with mapping labels
            pass
        else:
            # Read mapping information from the line
            dest, src, length = [int(i) for i in l.strip().split()]
            mapping.append(dict(src_first=src, src_last=src+length-1,
                                dest_first=dest, dest_last=dest+length-1))
    # Add the last mapping
    mappings.append(pd.DataFrame(mapping).sort_values(by='src_first'))

# Function to propagate a range through the mappings
def propagate_range(range, mapping):
    mapped_ranges = []
    i = 0
    while range != None and i < len(mapping):
        rule = mapping.iloc[i]
        if rule['src_first'] > range[1]:
            # No rule for the whole range
            mapped_ranges.append(range)
            range = None  # Nothing more to do
        elif range[0] < rule['src_first']:
            # No rule for part of the range
            mapped_ranges.append([range[0], rule['src_first']-1])
            range[0] = rule['src_first']
        elif range[0] <= rule['src_last']:
            if range[1] <= rule['src_last']:
                # The whole range is mapped using this rule
                offset = range[0] - rule['src_first']
                length = range[1] - range[0]
                new_start = rule['dest_first'] + offset
                mapped_ranges.append([new_start, new_start+length])
                range = None  # Nothing more to do
            else:
                # Only part of the range can be processed by this rule
                offset = range[0] - rule['src_first']
                length = rule['src_last'] - range[0]
                range[0] = rule['src_last']+1
                new_start = rule['dest_first'] + offset
                mapped_ranges.append([new_start, new_start+length])
        else:
            # range[0] > rule['src_last']
            # Try another rule
            i += 1
    if range != None:
        # We ran out of rules -> just return the remaining range as is
        mapped_ranges.append(range)
    return mapped_ranges

# Function to propagate seed ranges through all mappings
def propagate(seed_ranges, mappings):
    for mapping in mappings:
        new_ranges = []
        for i in range(len(seed_ranges)):
            new_ranges += propagate_range(list(seed_ranges.iloc[i]), mapping)
        seed_ranges = pd.DataFrame([dict(start=r[0], end=r[1]) for r in new_ranges]).sort_values(by='start')
    return seed_ranges.iloc[0]['start']

# Part 1
seed_ranges = pd.DataFrame([dict(start=s, end=s) for s in seeds]).sort_values(by='start')
print('Part 1:')
print(f'The lowest location number is {propagate(seed_ranges, mappings)}\n')

# Part 2
seed_ranges = pd.DataFrame([dict(start=s, end=s+l) for s, l in zip(seeds[::2], seeds[1::2])]).sort_values(by='start')
print('Part 2:')
print(f'The lowest location number is {propagate(seed_ranges, mappings)}')