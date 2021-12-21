player1 = 8
player2 = 4

dice = 0

score1 = 0
score2 = 0

while True:
    for _ in range(3):
        dice += 1
        player1 += dice
    player1 = player1 % 10
    if player1 == 0:
        player1 = 10
    score1 += player1
    if score1 >= 1000:
        break

    for _ in range(3):
        dice += 1
        player2 += dice
        player2 = player2 % 10
    if player2 == 0:
        player2 = 10
    score2 += player2
    if score2 >= 1000:
        break

print(f'dice={dice}, player1={score1}, player2={score2}')
if score1>=1000:
    print(f'loser*dice={dice*score2}')
else:
    print(f'loser*dice={dice*score1}')