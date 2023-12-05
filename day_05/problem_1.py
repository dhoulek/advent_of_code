from tqdm import tqdm
mappings = []
max_affected = 0

with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as 
# f:
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
            # max_affected = max([max_affected, src+length-1, dest+length-1])
    # add last mapping
    mappings.append(mapping)
            
# print(seeds)
# print(mappings)
# print(max_affected)

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
    
print('Part 1:')
print(f'The lowest location number is {min(final_locations)}\n')

# print(sum([s for s in seeds[1::2]])/150000/3600)
# print(sum([s for s in seeds[1::2]]))
# all_seeds = []
# for ini, length in zip(seeds[::2], seeds[1::2]):
#     print(ini>max_affected, ini+length>max_affected)
    # all_seeds += list(range(ini, ini+length))
    
# print(all_seeds)

lowest_location = int(1e10)
for ini, length in zip(seeds[::2], seeds[1::2]):
    for seed in tqdm(list(range(ini, ini+length))):
        # recipe = [seed]
        for mapping in mappings:
            for m in mapping:
                if m['src_first'] <= seed <= m['src_last']:
                    # found applicable map
                    seed += m['dest_first'] - m['src_first']
                    break
            # recipe.append(seed)
        # print(' -> '.join([str(s) for s in recipe]))
        lowest_location = min(lowest_location, seed)
        if lowest_location == 0:
            break
    
print('Part 2:')
print(f'The lowest location number is {lowest_location}')