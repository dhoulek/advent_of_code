count = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        count += sum([len(digit) in [2, 3, 4, 7] for digit in line.split('|')[-1].split()])
print(f'Answer is: {count}')