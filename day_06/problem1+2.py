with open ('input.txt', 'r') as f:
    input = [int(n) for n in f.readline().split(',')]

laternfish = [0 for i in range(9)]
for i in input:
    laternfish[i] += 1

print(f'initial distribution: {laternfish}')
for day in range(256):
    zero = laternfish[0]
    for i in range(6):
        laternfish[i] = laternfish[i+1]
    laternfish[6] = zero + laternfish[7]
    laternfish[7] = laternfish[8]
    laternfish[8] = zero
    if day in [17, 79, 255]:
        print(f'After {day+1:2d} days the distribution is: {laternfish}; the total number of laternfish is {sum(laternfish)}')
    