import random

# winner = ''
theBoard = {
    'top-L': ' ',
    'top-M': ' ',
    'top-R': ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'low-L': ' ',
    'low-M': ' ',
    'low-R': ' ',
}

def printBoard(board = theBoard):
    print(f" {board['top-L']} | {board['top-M']} | {board['top-R']}")
    print('-----------')
    print(f" {board['mid-L']} | {board['mid-M']} | {board['mid-R']}")
    print('-----------')
    print(f" {board['low-L']} | {board['low-M']} | {board['low-R']}")

def computer_move(board = theBoard):
    cell = random.choice(list(board))
    if board[cell] != ' ':
        return computer_move(board)
    else:
        board[cell] = 'O'
        return board


def check_win_cond(board):
    def sum(line):
        if (line == 'top' or line == 'mid' or line == 'low'):
            return board[f'{line}-L'] + board[f'{line}-M'] + board[f'{line}-R']
        if (line == 'L' or line == 'M' or line == 'R'):
            return board[f'top-{line}'] + board[f'mid-{line}'] + board[f'low-{line}']
        if(line == '/'):
            return board['low-L'] + board['mid-M'] + board['top-R']
        if(line == '\\'):
            return board['top-L'] + board['mid-M'] + board['low-R']

    lines = ['top', 'mid', 'low', 'L', 'M', 'R', '/', '\\']

    for line in lines:
        # print(f'{line} {sum(line)}')
        if sum(line) == 'OOO':
            return 'COMP'
        elif sum(line) == 'XXX':
            return 'PLAYER'
    return None

def still_spare_cells(board):
    for cell in board:
        if board[cell] == ' ':
            return True
    return False
# print(check_win_cond(theBoard))
# print(still_spare_cells(theBoard))

def player_move(board = theBoard):
    cell = input('Enter the empty cell with following syntax "top-L", "mid-M", "low-R"...eg. ')
    if cell not in board:
        return player_move(board)
    elif board[cell] != ' ':
        return player_move(board)
    else:
        board[cell] = 'X'
        return board

def should_game_continue(board = theBoard):
    global winner
    winner = check_win_cond(board)
    # print(f'DEBUG: {winner} in')
    if winner is not None:
        return False

    if still_spare_cells(board) is False:
        return False
    return True

print('Hello there! I see you wanna play Tic-Toc(not that zoomer stuff) with awesome randomized AI')
print('So lets beggin the battle, I know you are the kind man, so I let computer to be first')

while(True):
    
    if should_game_continue() is False:
        # print(f'DEBUG: {winner} out')
        break

    printBoard(computer_move())

    if should_game_continue() is False:
        # print(f'DEBUG: {winner} out')
        break

    player_move()

if winner == 'PLAYER':
    print('WIN!!!')
elif winner == 'COMP':
    print('LOSER !')
else:
    print('SPAR ?!')