def convert(s):    
    if isinstance(s, (int, list)):
        return s
    elif s.isnumeric():
        return int(s)
    else:
        level = 0
        split = []
        st = ''
        for c in s[1:-1]:
            if c == '[':
                st += c
                level += 1
            elif c == ']':
                st += c
                level -= 1
            elif c == ',' and level == 0:
                split.append(convert(st))
                st = ''
            else:
                st += c
        if st != '':
            split.append(convert(st))

        return split


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        # both numbers, let's compare
        if left<right:
            # correct order
            return 1 
        elif left>right:
            # wrong order
            return -1
        else:
            # continue
            return 0
    else:
        # check if one of them is a number only -> list
        if isinstance(left, int):
            left = [left]            
        elif isinstance(right, int):
            right = [right]
        # now both are lists, compare item by item
        for i in range(min(len(left), len(right))):
            # print('>>', left, right)
            l = left[i]
            r = right[i]
            # print('**', l, r, left, right)
            result = compare(l, r)
            if result != 0:
                return result
                break
        # end of list comparison and no decision
        if len(left) == len(right):
            # same length, continue
            # print('** 0', left, right)
            return 0
        elif len(left) < len(right):
            # correct order
            # print('** 1', left, right)
            return 1
        else:
            # wrong order
            # print('** -1', left, right)
            return -1

lines = [[[2]], [[6]]]
with open('input.txt', 'r') as f:
    for line in f. readlines():
        line = line.strip()
        if len(line)>0:
            lines.append(convert(line))
# print(lines)

# implementing bubble sort
cycle = 0
done = False
while not done:
    done = True
    cycle += 1    
    print(f'Sorting cycle {cycle}')
    # for l in lines:
    #     print(' ', l)
    for i in range(len(lines)-1):
        # print(" ", lines[i], lines[i+1])
        comp_res = compare(lines[i], lines[i+1])
        # print(comp_res, lines[i], lines[i+1])
        if comp_res < 0:
            # print(f'changing {i} and {i+1}')
            done = False
            l = lines[i].copy()
            lines[i] = lines[i+1].copy()
            lines[i+1] = l.copy()

print(f'Final order:')
key = 1
for i, l in enumerate(lines):
    if l in [[[2]], [[6]]]:
        key *= (i+1)
    print(f'{i+1}: {l}')
print(f'decoder key for the distress signal is {key}')