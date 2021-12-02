def decode(string):
    row = int(string[:7].replace('B', '1').replace('F', '0'), 2)
    column = int(string[-3:].replace('R', '1').replace('L', '0'), 2)
    return(column+row*8)

# print(decode('BFFFBBFRRR'))
# print(decode('FFFBBBFRRR'))
# print(decode('BBFFBBFRLL'))
    
with open('5.in', 'r') as input:
    print(max([decode(line.rstrip()) for line in input.readlines()]))
    
with open('5.in', 'r') as input:
    ids = sorted([decode(line.rstrip()) for line in input.readlines()])
for i in range(1, len(ids)-1):
    if (2*ids[i] != ids[i-1]+ids[i+1]):
        print(ids[i-1], ids[i], ids[i+1])
    