def tobogan(right, down):
    input = open('3.in', 'r')
    pos = 0
    trees = 0
    linecount = 0    
    for line in input.readlines():
        line = line.strip()
        # print(pos, len(line), pos % len(line), line[pos % len(line)])
        # print(linecount % down)
        if linecount % down == 0:
            if line[pos % len(line)] == '#':
                trees += 1
            pos += right
        linecount +=1
    input.close()
    return trees

# print(tobogan(1, 1))
print(tobogan(3, 1))
# print(tobogan(5, 1))
# print(tobogan(7, 1))
# print(tobogan(1, 2))

print(tobogan(1, 1) * tobogan(3, 1) * tobogan(5, 1) * tobogan(7, 1) * tobogan(1, 2))