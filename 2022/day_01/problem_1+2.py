elves = []
with open('input.txt', 'r') as f:
    cal = 0
    for line in f.readlines():
        if line.strip() == '':
            elves.append(cal)
            cal = 0
        else:
            cal += int(line.strip())
elves.append(cal)

# problem 1
print(f'Number of Elves: {len(elves)}')
print(f'Maximum calories: {max(elves)}')
print(f'Carried by Elf number: {elves.index(max(elves))+1}')

# problem 2
print(f'Top three Elves carry together {sum(sorted(elves)[-3:])} calories')
