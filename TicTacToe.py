####################
# global variables #
####################

cur_player = 0

players = {
    'marker': ['', ''],
    'score': [0, 0]
}

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
            

# display_board(test_board)
choose_marker()
