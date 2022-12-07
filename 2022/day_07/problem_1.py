fs = [{
       'name': '/',
       'content': {},
       'size': None,
       'prev': None
       }]
curr = 0

ls = False
with open('test.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        if ls:
            # listing content mode
            if line[0] == '$':
                # end of listing
                ls = False
            else:
                print(line)
        if not ls:
            # command mode:
            if line[1] == 'ls':
                # start listing
                ls = True
            elif line[1] == 'cd':
                # change directory
                # if not yet added, add it                
                if line[2] not in fs[curr]['content'].items() and line[2] not in ['/', '..']:
                    print('adding', line[2])                                            
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
                    
print(fs)