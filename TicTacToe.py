board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

turn = ''

def draw_board(board):
    print("  a   b   c")
    print("1 " + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('  ---------')
    print("2 " + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('  ---------')
    print("3 " + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])

def user_turn(isFirstTurn, isError):
    global turn
    if isFirstTurn:
        turn = input("Is it a x or o turn? ")
        if turn.lower() != 'x' and turn.lower() != 'o':
            print("Invalid input, has to be x or o")
            user_turn(True, True)
    elif isError == True:
        turn = turn
    else:
        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'

    row = input("Please enter a letter between a and c: ").lower()
    if row not in ['a', 'b', 'c']:
        print("Invalid input, has to be between a and c")
        user_turn(False, True)

    if   row == 'a': row = 0
    elif row == 'b': row = 1
    elif row == 'c': row = 2

    column = int(input("Please enter a letter between 1 and 3: "))
    if column < 1 and column > 3:
        print("Invalid input, has to be between 1 and 3")
        user_turn(False, True)

    if board[column - 1][row] == '_':
        board[column - 1][row] = turn
    else:
        print("Invalid input, has to be an empty space")
        user_turn(False, True)

def check_win(board):
    if board[0][0] == board[0][1] == board[0][2] != '_':
        return True
    elif board[1][0] == board[1][1] == board[1][2] != '_':
        return True
    elif board[2][0] == board[2][1] == board[2][2] != '_':
        return True
    elif board[0][0] == board[1][0] == board[2][0] != '_':
        return True
    elif board[0][1] == board[1][1] == board[2][1] != '_':
        return True
    elif board[0][2] == board[1][2] == board[2][2] != '_':
        return True
    elif board[0][0] == board[1][1] == board[2][2] != '_':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != '_':
        return True
    else:
        return False

def isFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return False
    return True

def main():
    global board
    user_turn(True, False)
    while not check_win(board) and not isFull(board):
        draw_board(board)
        user_turn(False, False)
    
    if not isFull(board):
        print("The winner is: " + turn)
        draw_board(board)
    else:
        print("It's a draw!")
        again = input("Would you like to play again (y/n)? ")
        if again.lower() == 'y':
            board = [['_', '_', '_'],
                     ['_', '_', '_'],
                     ['_', '_', '_']]
            main()

__name__ == '__main__' and main()