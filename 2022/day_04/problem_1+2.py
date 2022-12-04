count = 0
count2 = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        p1, p2 = line.strip().split(',')
        p1s, p1e = [int(x) for x in p1.split('-')]
        p2s, p2e = [int(x) for x in p2.split('-')]
        if (p1s<=p2s and p1e>=p2e) or (p1s>=p2s and p1e<=p2e):
            count += 1
        if (p1s<=p2e and p1e>=p2s) or (p1s<=p2e and p1s>=p2e):
            print(line)
            count2 += 1
print(f'There are {count} fully overllaping ranges')
print(f'There are {count2} overllaping ranges')