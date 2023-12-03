strategy = {
       'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'},
       'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
       'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
       }
score_shape = {
    'X': 1,
    'Y': 2,
    'Z': 3
    }

score = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        he, output = line.split()
        me = strategy[he][output]
        this_round = score_shape[me]
        if output == 'Y':
            this_round += 3
        elif output == 'Z':
            this_round += 6
        score += this_round
        print(he, me, this_round, score)
        