from numpy import array, ceil, floor, str

def norm(v):
    return max([abs(i) for i in v])

def to_int(v):
    return array([int(ceil(i)) if i>0 else int(floor(i)) for i in v])

rope  = [array([0, 0]) for _ in range(10)]

visited = {str(rope[-1])}

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        if line[0] == 'R':
            move = array([1, 0])
        elif line[0] == 'L':
            move = array([-1, 0])
        elif line[0] == 'U':
            move = array([0, 1])
        else:
            move = array([0, -1])
        for _ in range(int(line[1])):            
            rope[0] += move
            # print(rope)
            for i in range(1, 10):
                dir = rope[i-1] - rope[i]
                if norm(dir)>1:
                    rope[i] += to_int(dir/2)
            visited = visited.union({str(rope[-1])})
        # print([str(i) for i in rope])
print('tail visited', len(visited),'positions')