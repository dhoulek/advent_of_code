win = {
       'X': 'C',
       'Y': 'A',
       'Z': 'B'
       }
draw = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
        }
score_shape = {
    'X': 1,
    'Y': 2,
    'Z': 3
    }

score = 0
with open('input.txt', 'r') as f:
    for line in f.readlines():
        he, me = line.split()
        this_round = score_shape[me]
        if draw[me] == he:
            this_round += 3
        elif win[me] == he:
            this_round += 6
        score += this_round
        print(he, me, this_round, score)
        