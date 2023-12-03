s = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        n = len(line)//2
        part1 = set(line[:n])
        part2 = set(line[n:])
        item = list(part1.intersection(part2))[0]
        if item<'a':
            v = ord(item)-ord('A')+27            
        else:
            v = ord(item)-ord('a')+1
        s += v
        print(item, v, s)