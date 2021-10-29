###
### Author: Xin Li.
### Description: In this PA, i will be implementing
### a simpler variant of chess: 1D Chess! 1D chess is
### a variant of the game that is played on a board
### that has only one column of spaces, rather than
### a grid of spaces, as in typical chess. There are
### actually multiple variants of 1D chess. In this
### PA, i implement a custom variant of 1D
### chess.
###

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    if 0 <= position and position <=8:
        if player==WHITE:
            if board[position]==W_KNIGHT or board[position]==W_KING:
                return True
            else:
                return False
        if player==BLACK:
            if board[position]==B_KNIGHT or board[position]==B_KING:
                return True
            else:
                return False
    return False
def move_knight(board, position, direction):
    if direction=='r':
        board[position+2]=board[position]
        board[position]=EMPTY
    if direction=='l':
        board[position-2]=board[position]
        board[position]=EMPTY

def move_king(board, position, direction):
    if direction=='r':
        for i in range(1,8):
            if board[position+i]!=EMPTY:
                board[position+i]=board[position]
                board[position]=EMPTY
                break
            elif position+i==8:
                board[8]=board[position]
                board[position]=EMPTY
                break
    if direction=='l':
        for i in range(1,8):
            if board[position-i]!=EMPTY:
                board[position-i]=board[position]
                board[position]=EMPTY
                break
            elif position-i==0:
                board[0]=board[position]
                board[position]=EMPTY
                break

def print_board(board):
    print('+','-'*53,'+',sep='')
    print('| ',board[0],' | ',board[1],' | ',board[2],' | ',board[3],' | ',board[4],' | ',board[5],' | ',board[6],' | ',board[7],' | ',board[8],' | ',sep='')
    print('+','-'*53,'+',sep='')

def get_color(piece):
    if piece == W_KNIGHT or piece == W_KING:
        return 'white'
    return 'black'

def get_piece(piece):
    if piece == W_KNIGHT or piece == B_KNIGHT:
        return 'knight'
    elif piece == W_KING or piece == B_KING:
        return 'king'
def draw_board(board, gui):
    gui.text(200, 40, '1 Dimensional Chess', 'green', 25)
    gui.rectangle(40, 100, 590, 70, 'brown')
    gui.text(55, 120, get_piece(board[0]), get_color(board[0]), 15)
    gui.line(115, 100, 115, 170, 'black')
    gui.text(120, 120, get_piece(board[1]), get_color(board[1]), 15)
    gui.line(180, 100, 180, 170, 'black')
    gui.text(185, 120, get_piece(board[2]), get_color(board[2]), 15)
    gui.line(245, 100, 245, 170, 'black')
    gui.text(250, 120, get_piece(board[3]), get_color(board[3]), 15)
    gui.line(310, 100, 310, 170, 'black')
    gui.text(315, 120, get_piece(board[4]), get_color(board[4]), 15)
    gui.line(375, 100, 375, 170, 'black')
    gui.text(380, 120, get_piece(board[5]), get_color(board[5]), 15)
    gui.line(440, 100, 440, 170, 'black')
    gui.text(445, 120, get_piece(board[6]), get_color(board[6]), 15)
    gui.line(505, 100, 505, 170, 'black')
    gui.text(510, 120, get_piece(board[7]), get_color(board[7]), 15)
    gui.line(570, 100, 570, 170, 'black')
    gui.text(575, 120, get_piece(board[8]), get_color(board[8]), 15)
    gui.update_frame(30)

def is_game_over(board):
    if W_KING in board:
        if B_KING not in board:
            print_board(board)
            print('White wins!')
            return True
        else:
            return False
    if B_KING in board:
        if W_KING not in board:
            print_board(board)
            print('Black wins!')
            return True
        else:
            return False

def move(board, position, direction):
    if board[position]==W_KING or board[position]==B_KING:
        move_king(board, position, direction)
    if board[position]==W_KNIGHT or board[position]==B_KNIGHT:
        move_knight(board, position, direction)

def main():

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]

    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')
        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)

main()
