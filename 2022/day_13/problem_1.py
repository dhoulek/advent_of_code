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
            l = left.pop(0)
            r = right.pop(0)
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

with open('input.txt', 'r') as f:
    eof = False
    pair = 0
    sum_of_correct = 0
    while not eof:
        pair += 1
        left = convert(f.readline().strip())
        right = convert(f.readline().strip())
        # print(left, right)
        eof = not f.readline()
        # eof=True
        if compare(left, right) == 1:
            # print(' ', left)
            # print(' ', right)
            sum_of_correct += pair
            print(f'Pair in correct order: {pair}')
print(f'Sum of correct-order pairs: {sum_of_correct}')