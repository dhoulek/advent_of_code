from itertools import product

throws = [x+y+z for x,y,z in product(range(1,4), range(1,4), range(1,4))]
results = set(throws)
multi = {}
for r in results:
    i = 0
    for v in throws:
        if v == r:
            i += 1
    multi[r] = i
    
def play_round(player, player1, player2, score1, score2):
    win1 = 0
    win2 = 0
    if player == 1:
        for r in results:
            pos = player1+r
            pos = pos % 10
            if pos == 0:
                pos = 10
            score = score1+pos
            if score >= 21:
                w1 = 1
                w2 = 0
            else:
                w1, w2 = play_round(2, pos, player2, score, score2)
            win1 += w1*multi[r]
            win2 += w2*multi[r]
    else:
        for r in results:
            pos = player2+r
            pos = pos % 10
            if pos == 0:
                pos = 10
            score = score2+pos
            if score >= 21:
                w1 = 0
                w2 = 1
            else:
                w1, w2 = play_round(1, player1, pos, score1, score)
            win1 += w1*multi[r]
            win2 += w2*multi[r]
    return win1, win2
    
    
    
print(multi)
w1, w2 = play_round(1, 8, 4, 0, 0)
print(f'player 1 wins {w1} times')
print(f'player 2 wins {w2} times')