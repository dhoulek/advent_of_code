from tqdm import tqdm

with open('test.txt', 'r') as f:
    input = f.readlines()
workflows = {}
l = str.strip(input.pop(0))
while l != '':
    node, l = l.split('{')
    conds = l.split(',')
    for i in range(len(conds)-1):
        c, r = conds[i].split(':')
        conds[i] = [c[0], c[1], int(c[2:]), r]
    conds[-1] = conds[-1][:-1]
    workflows[node] = conds
    l = str.strip(input.pop(0))
# print(workflows)

def process_workflow(wf, part):
    wf = workflows[wf]
    for r in wf[:-1]:
        if (r[1] == '<'  and  part[r[0]] < r[2])  or  ((r[1] == '>'  and  part[r[0]] > r[2])):
            return r[3]
    return wf[-1]

print('Part 1:')
processed = []
checksum = 0
for l in tqdm(input):
    l = l.strip()[1:-1].split(',')
    part = {}
    for v in l:
        v = v.split('=')
        part[v[0]] = int(v[1])
    wf = 'in'
    wfs = [wf]
    while wf not in ['A', 'R']:
        wf = process_workflow(wf, part)
        wfs.append(wf)
    # print(part, wfs)
    if wfs[-1] == 'A':
        checksum += sum(part.values())
print(f'Sum of all input values of all accepted parts is {checksum}')

# print(len(workflows))
parts = {c: [1, 4000] for c in list('xmas')}

def count_workflow(wf, parts, used):
    if wf in used:
        # this workflow was already used, break
        print('reused wf')
        return 0
    elif wf == 'A':
        acc = 1
        for m, M in parts.values():
            acc *= (M-m+1)
        print(used)
        return acc
    elif wf == 'R':
        return 0
    else:
        used.append(wf)
        wf = workflows[wf]
        acc = 0
        for r in wf[:-1]:
            c = r[0]
            if r[1] == '<' and parts[c][0] < r[2]:
                a_parts = parts.copy()
                a_parts[c][1] = min(a_parts[c][1], r[2]-1)            
                acc += count_workflow(r[3], a_parts, used)
                if a_parts[c][1] == parts[c][1]:
                    # no rejected parts
                    break
                else:
                    # get limits for rejected parts and continue to the next rule
                    parts[c][0] = parts[c][1]+1
            elif r[1] == '>' and parts[c][1] > r[2]:
                a_parts = parts.copy()
                a_parts[c][0] = max(a_parts[c][0], r[2]+1)            
                acc += count_workflow(r[3], a_parts, used)
                if a_parts[c][0] == parts[c][0]:
                    # no rejected parts
                    break
                else:
                    # get limits for rejected parts and continue to the next rule
                    parts[c][1] = parts[c][0]-1
            else:
                # no accepted parts, continues with next rule
                pass
        # add final condition
        acc += count_workflow(wf[-1], parts, used)
        return acc
    
print(count_workflow('in', parts, []))
print(4000**4)
# }
print('Part 2:')