with open('input.txt', 'r') as f:
    line = f.readline().strip()
    
i = 0
while i<len(line)-3:
    m = line[i:i+4]
    if len(set(m)) == 4:
        print(f'First marker is finished after {i+4} characters')
        break
    i += 1