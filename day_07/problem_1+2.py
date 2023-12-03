fs = [{
       'name': '/',
       'content': {},
       'size': None,
       'prev': None
       }]
curr = 0

ls = False
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        if ls:
            # listing content mode
            if line[0] == '$':
                # end of listing
                ls = False
            else:
                # add listed content
                if line[1] not in fs[curr]['content'].items():
                    # print('adding', line[1])  
                    if line[0] == 'dir':
                        # adding directory
                        fs.append({
                           'name': line[1],
                           'content': {},
                           'size': None,
                           'prev': curr
                           })
                        fs[curr]['content'][line[1]] = len(fs)-1
                    else:
                        # adding file
                        fs.append({
                           'name': line[1],
                           'content': None,
                           'size': int(line[0]),
                           'prev': curr
                           })
                        fs[curr]['content'][line[1]] = len(fs)-1
        if not ls:
            # command mode:
            if line[1] == 'ls':
                # start listing
                ls = True
            elif line[1] == 'cd':
                # change directory
                # if not yet added, add it                
                if line[2] not in fs[curr]['content'].keys() and line[2] not in ['/', '..']:
                    # print('adding', line[2])                                            
                    fs.append({
                       'name': line[2],
                       'content': {},
                       'size': None,
                       'prev': curr
                       })
                    fs[curr]['content'][line[2]] = len(fs)-1
                if line[2] not in ['/', '..']:
                    curr = fs[curr]['content'][line[2]]
                elif line[2] == '..':
                    curr = fs[curr]['prev']                   
# print(fs)

# get sizes of all parts of the file system
unknown = 1
while unknown > 0:
    unknown = 0
    for i in reversed(range(len(fs))):
        if fs[i]['size'] == None:
            size = 0
            done = True
            for j in fs[i]['content'].values():
                if fs[j]['size'] == None:
                    done = False
                    break
                else:
                    size += fs[j]['size']        
            if done:
                fs[i]['size'] = size
            else:
                unknown += 1
    # print('Unknown sizes:', unknown)
    
# now solve the puzzle 1
size = 0
for i in fs:
    if i['content'] != None:
        # we found a directory!
        if i['size'] <= 100000:
            # print(i)
            size += i['size']
            
print('total size of small directories is', size)

# now solve the puzzle 2
needed =  30000000 - (70000000 - fs[0]['size'])
print('space needed for update:', needed)
# get list of potential directories
candidates = {}
for n, i in enumerate(fs):
    if i['content'] != None:
        # we found a directory!
        if i['size'] >= needed:
            # print(i)
            candidates[n] = i['size']
to_delete = min(candidates.values())
print('you should delete directory with size', to_delete)