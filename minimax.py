#!/usr/bin/python

inf = 999 # infinity

# displays current bard position
def print_board(board):
    for i in board:
        row = ""
        for j in i:
            row += (j + " ")
        print(row)

# utility function, determines if the game is finished
def game_over(board):

    ld_count = 0
    rd_count = 0
    count = 0 # total piece count
    for i in range(3):
        h_count = 0 # horizontal count
        v_count = 0 # vertical count
        for j in range(3):
            # horizontal
            if board[i][j] == "X":
                h_count += 1
                count += 1
            elif board[i][j] == "O":
                h_count -= 1
                count += 1
            # vertical
            if board[j][i] == "X":
                v_count += 1
            elif board[j][i] == "O":
                v_count -= 1
            # left diagonal
            if i == j:
                if board[i][j] == "X":
                    ld_count += 1
                elif board[i][j] == "O":
                    ld_count -= 1
            # right diagonal
            if i == 2 - j:
                if board[i][j] == "X":
                    rd_count += 1
                elif board[i][j] == "O":
                    rd_count -=1

        if h_count == 3 or h_count == -3 or v_count == 3 or v_count == -3:
            return True
    if ld_count == 3 or ld_count == -3 or rd_count == 3 or rd_count == -3:
        return True

    if count == 9:
        return True # if no more positions available

    return False # if the game isn't over

# utility function, values a  given count
def evaluate_count(count):
    value = 0

    if count == 1: # Xs
        value -= 1
    elif count == 2:
        value -= 10
    elif count == 3:
        value -= 100
    elif count == 4: # Os
        value += 1
    elif count == 8:
        value += 10
    elif count == 12:
        value += 100

    return value

# function evaluates the current position
def evaluate(position):
    value = 0 # position value

    ld_count = 0 # left diagonal
    rd_count = 0 # right diagonal
    for i in range(3):
        h_count = 0 # horizontal count
        v_count = 0 # vertical count
        for j in range(3):
            # checks horizontal
            if position[i][j] == "X":
                h_count += 1
            elif position[i][j] == "O":
                h_count += 4

            # checks vertical
            if position[j][i] == "X":
                v_count += 1
            elif position[j][i] == "O":
                v_count += 4

            # checks left diagonal
            if i == j:
                if position[i][j] == "X":
                    ld_count += 1
                elif position[i][j] == "O":
                    ld_count += 4

            if i == 2 - j:
                if position[i][j] == "X":
                    rd_count += 1
                elif position[i][j] == "O":
                    rd_count += 4

        # horizontal analysis
        value += evaluate_count(h_count)
        # vertical analysis
        value += evaluate_count(v_count)
    
    # left diagonal analysis
    value += evaluate_count(ld_count)
    # right diagonal analysis
    value += evaluate_count(rd_count)

    return value

# calculates all possible moves from current position
def get_children(position, max_player):
    
    if max_player:
        team = "O"
    else:
        team = "X"
    
    children = [] # empty set to store children
    for i in range(3):
        for j in range(3):
            if position[i][j] != "X" and position[i][j] != "O":
                child = [row[:] for row in position]
                child[i][j] = team
                children.append(child)

    return children

# function calculates a specified number of moves ahead (depth) 
# to predict the best move
def minimax(position, depth, max_player):

    if depth == 0 or game_over(position):
        return position
   
    # if current turn is maximizing player
    if max_player:
        max_eval = -1 * inf
        children = get_children(position, max_player)
        max_pos = children[0] # set to first possible move
        for child in children:
            pos = minimax(child, depth-1, False)
            evaluation = evaluate(pos)
            # compares the current evaluation to the one calculated
            if evaluation > max_eval:
                max_eval = evaluation
                max_pos = child
        return max_pos

    # current turn is minimizign player
    else:
        min_eval = inf
        children = get_children(position, max_player)
        min_pos = children[0] # set to the first possible move
        for child in children:
            pos = minimax(child, depth-1, True)
            evaluation = evaluate(pos)
            # compares the current evaluation to the one calculated
            if evaluation < min_eval:
                min_eval = evaluation
                min_pos = child
        return min_pos

def main(): 
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    print_board(board)
    
    while not game_over(board):
        x = -1
        y = -1
        while True:
            x_pos, y_pos = raw_input("Move: ").split()
            x = int(x_pos) - 1
            y = int(y_pos) - 1
            if (x < 0 or x > 2) or (y < 0 or y > 2):
                print
                print "Out of bounds"
                continue
            elif board[y][x] != "-":
                print
                print "Invalid position"
                continue
            break

        board[y][x] = "X"
        print_board(board)
        print

        board = minimax(board, 10, True)
        print_board(board)
        print

main()
