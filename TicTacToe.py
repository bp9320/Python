####################
# global variables #
####################

cur_player = 0

players = {
    'marker': ['', ''],
    'squares': [[],[]]
}

game_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']

winning_combos = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))

game_is_afoot = True

test_board = ['#','X','O','X','O','X','O','X','O','X']

##################
# Game Functions #
##################

def display_board(board):

    '''
    Displays tic-tac-toe board.
        board: list containing the value of each square on the board
    '''

    vertical_divider = '   |   |   \n'
    horizontal_divider = '-----------\n'
    top_cells = f' {board[7]} | {board[8]} | {board[9]} \n'
    mid_cells = f' {board[4]} | {board[5]} | {board[6]} \n'
    bot_cells = f' {board[1]} | {board[2]} | {board[3]} \n'

    print('\n',
        vertical_divider, top_cells, vertical_divider,
        horizontal_divider,
        vertical_divider, mid_cells, vertical_divider,
        horizontal_divider,
        vertical_divider, bot_cells, vertical_divider
        )

def choose_marker():
    done = False
    marker = ''
    while not done:
        marker = input('Player 1: Choose your marker by entering X or O \t').lower()

        if marker == 'x':
            players['marker'][0] = 'X'
            players['marker'][1] = 'O'
            done = True

        elif marker == 'o':
            players['marker'][0] = 'O'
            players['marker'][1] = 'X'
            done = True

def get_square(player):
    valid = False
    square = 0
    while not valid:
        square = int(input(f'Player {player + 1}: Choose an open square:\t'))
        if square >= 1 and square <= 9:
            valid = True
        else:
            print('Please choose an unoccupied square between 1 and 9 inclusive.')
    return square

def update_board():
    global cur_player
    global game_board
    global players

    position = get_square(cur_player)

    if str(position) not in game_board:
        print('That square has already been chosen.')
        position = get_square(cur_player)
    else:
        players['squares'][cur_player].append(position)
        game_board[position] = players['marker'][cur_player]



def check_winner(player_squares):
    global cur_player
    for combo in winning_combos:
        for num in combo:
            # print(cur_player)
            # print (player_squares)
            # print (players['squares'][cur_player])
            # print(combo, num)
            if num not in player_squares:
                break
            if num in player_squares and num == combo[-1]:
                return True
    if cur_player == 0:
        cur_player += 1
    else:
        cur_player -= 1

    return False



def reset_game():
    global game_board
    global cur_player
    global players
    game_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cur_player = 0
    players = {
        'marker': ['', ''],
        'squares': [[],[]]
    }


# display_board(test_board)
# choose_marker()
# get_square(cur_player)

def play_game():
    global game_is_afoot

    choose_marker()

    while game_is_afoot:
        display_board(game_board)
        update_board()
        print(cur_player, check_winner(players['squares'][cur_player]))
        if(check_winner(players['squares'][cur_player])):
            print(f'PLAYER {cur_player + 1} WINS!!!!')
            game_is_afoot = False

play_game();
# print(check_winner([1,2,3]))