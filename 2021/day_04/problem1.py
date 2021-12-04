with open('input.txt') as f:
    draws = [int(n) for n in f.readline().split(',')]
    i = 0
    boards = []
    for line in f.readlines():
        if i == 0:
            board = []
        else:
            board.append([int(n) for n in line.strip().split()])
        if i == 5:
            boards.append(board)
            i = 0
        else:
            i += 1

print(f'{len(draws)} numbers in the draw')
print(f'{len(boards)} boards')

if len(boards[-1]) != 5:
    print('something wrong with the input: last board doesn have the shape of 5x5')
    print(boards[-1])
    quit()

def eval_board(board):
    rows = [sum(board[i]) for i in range(5)]
    cols = [sum([board[i][j] for i in range(5)]) for j in range(5)]
    return rows, cols

bingo = False
while not bingo:
    draw = draws[0]
    draws = draws[1:]
    
    for b, board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == draw:
                    boards[b][i][j] = 0
        rows, cols = eval_board(board)
        this_bingo = 0 in rows+cols
        if this_bingo:
            answer = sum(rows)*draw
        bingo = bingo or this_bingo
        
print(f'answer is: {answer}')