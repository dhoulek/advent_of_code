s = 0

c = 0
all_chars = set([chr(i+ord('a')) for i in range(26)] + [chr(i+ord('A')) for i in range(26)])
badge = all_chars

with open('input.txt', 'r') as f:    
    for line in f.readlines():
        badge = badge.intersection(set(line))
        c += 1
        if c == 3:
            badge = list(badge)[0]
            if badge<'a':
                v = ord(badge)-ord('A')+27            
            else:
                v = ord(badge)-ord('a')+1
            s += v
            print(badge, v, s)
            c = 0
            badge = all_chars