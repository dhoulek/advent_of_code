from numpy import array

forrest = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        forrest.append([int(x) for x in line])
forrest = array(forrest)

# get forrest dimensions - it is a square 
N = len(forrest)

# all trees on sides are visible
visible = 4*(N-1)

# let's check the interior
for i in range(1, N-1):
    for j in range(1, N-1):
        if forrest[i, j] > min([max(forrest[i, :j]), max(forrest[i, j+1:]),
                                 max(forrest[:i, j]), max(forrest[i+1:, j])]):
            visible += 1
print('visible positions:', visible)

# getting viewving distances
best_score = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        score = 1
        for row in [reversed(forrest[i, :j]), forrest[i, j+1:], reversed(forrest[:i, j]), forrest[i+1:, j]]:
            d = 0
            for tree in row:
                d += 1
                if tree >= forrest[i,j]:
                    break
            score *= d
        best_score = max([best_score, score])
print('best viewing score is', best_score)