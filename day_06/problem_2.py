with open('input.txt', 'r') as f:
    line = f.readline().strip()
    
i = 0
while i<len(line)-13:
    m = line[i:i+14]
    if len(set(m)) == 14:
        print(f'First marker is finished after {i+14} characters')
        break
    i += 1