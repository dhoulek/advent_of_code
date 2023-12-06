# Brute force solution for propagating seed by seed. Took about 1 hrs on mul-hpc-8.1, 6 core node

from multiprocessing import Pool
mappings = []

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    # reading seeds
    seeds = [int(i) for i in f.readline().strip().split(':')[-1].split()]
    
    # reading recipes
    mapping = []
    for l in f.readlines():        
        if l.strip() == '':
            # new mapping
            if len(mapping) > 0:
                # this is not the first mapping; add the previous to the list
                mappings.append(mapping)
            mapping = []
        elif l.strip()[-1] == ':':
            # mapping label; skip
            pass
        else:
            # read mapping
            dest, src, length = [int(i) for i in l.strip().split()]
            mapping.append(dict(src_first=src, src_last=src+length-1, 
                                dest_first=dest, dest_last=dest+length-1))
    # add last mapping
    mappings.append(mapping)

# Part 1
print('Part 1:')

# List to store final locations after applying mappings            
final_locations = []
for seed in seeds:
    recipe = [seed]
    for mapping in mappings:
        for m in mapping:
            if m['src_first'] <= seed <= m['src_last']:
                # found applicable map
                seed += m['dest_first'] - m['src_first']
                break
        recipe.append(seed)
    # print(' -> '.join([str(s) for s in recipe]))
    final_locations.append(recipe[-1])
    
print(f'The lowest location number is {min(final_locations)}\n')



# Part 2
print('Part 2:')

# Function to apply mappings to a seed
def propagate(seed):
    for mapping in mappings:
        for m in mapping:
            if m['src_first'] <= seed <= m['src_last']:
                # Found applicable map
                seed += m['dest_first'] - m['src_first']
                break
    return seed

lowest_location = int(1e10)
i = 0
for ini, length in zip(seeds[::2], seeds[1::2]):
    i += 1
    print(f' Processing range {i}/{len(seeds)//2}, of length {length}')
    
    # Use multiprocessing to apply mappings to a range of seeds
    with Pool() as pool:
        mapped_range = pool.map(propagate, range(ini, ini+length))
        
    lowest_location = min(lowest_location, min(mapped_range))
    if lowest_location == 0:
        break
    
print(f'The lowest location number is {lowest_location}')