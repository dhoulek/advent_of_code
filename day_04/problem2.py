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

bingos = [0 for b in boards]
all_bingos = False
round = 0
while not all_bingos:
    round += 1
    draw = draws[0]
    draws = draws[1:]
    
    for b, board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == draw:
                    boards[b][i][j] = 0
        rows, cols = eval_board(board)
        this_bingo = 0 in rows+cols
        if this_bingo and bingos[b] == 0:
            answer = sum(rows) * draw
            bingos[b] = 1
            print(f'board {b+1} gets bingo in round {round} by drawing {draw} with answer {answer}; remaining boards: {len(bingos)-sum(bingos)}')
    all_bingos = sum(bingos) == len(bingos)
        
print(f'answer is: {answer}')