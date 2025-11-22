"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player1 = 0
    player2 = 0
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == X:
                player1 += 1
            if board[row][column] == O:
                player2 += 1
    if player1 > player2:
        return O
    else:
        return X   


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act = set()

    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == EMPTY:
                act.add((row,column))

    return act


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row = action[0]
    column = action[1]

    if board[row][column] != EMPTY:
        raise 'Illegal move!'

    new_board = copy.deepcopy(board)

    new_board[row][column] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    for n in range(0,3):
        # Checks for rows
        if board[n][0] == board[n][1] and board[n][1] == board[n][2] and board[n][0] != None:
            return True
        # Check for columns
        if board[0][n] == board[1][n] and board[1][n] == board[2][n] and board[0][n] != None:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
        return True
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != None:
        return True
    
    # Checks to see if there are any empty spaces
    for row in board:
        if EMPTY in row:
            return False

    else:
        return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    for n in range(0,3):
        # Checks for rows
        if board[n][0] == board[n][1] and board[n][1] == board[n][2]:
            if board[n][0] == X:
                return 1
            elif board[n][0] == O:
                return -1
        # Check for columns
        if board[0][n] == board[1][n] and board[1][n] == board[2][n]:
            if board[0][n] == X:
                return 1
            elif board[0][n] == O:
                return -1
    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[1][1] == X:
            return 1
        elif board[1][1] == O:
            return -1
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        if board[1][1] == X:
            return 1
        elif board[1][1] == O:
            return -1
    else:
        return 0


def minimax(board):
    _, move = find_minimax(board)
    return move

def find_minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        if terminal(board):
            return utility(board), None
        v = -100
        opt_move = None
        for move in actions(board):
            v_loc, new_move = find_minimax(result(board, move))
            if v < v_loc:
                v = v_loc
                opt_move = move
                if v == 1:
                    return v, opt_move
        return v, opt_move
    
    if player(board) == O:
        if terminal(board):
            return utility(board), None
        v = 100
        opt_move = None
        for move in actions(board):
            v_loc, new_move = find_minimax(result(board, move))
            if v > v_loc:
                v = v_loc
                opt_move = move
                if v == -1:
                    return v, opt_move
        return v, opt_move


if __name__ == "__main__":
    test_board=[[ 'X', 'O', EMPTY], [ EMPTY, 'X', EMPTY], [EMPTY, EMPTY, 'O']]
    x=minimax(test_board)
    print(x)


