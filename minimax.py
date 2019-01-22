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
        if h_count == 3 or h_count == -3 or v_count == 3 or v_count == -3:
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

    ldCount = 0 # left diagonal
    rdCount = 0 # right diagonal
    for i in range(3):
        hCount = 0 # horizontal count
        vCount = 0 # vertical count
        for j in range(3):
            # checks horizontal
            if position[i][j] == "X":
                hCount += 1
            elif position[i][j] == "O":
                hCount += 4

            # checks vertical
            if position[j][i] == "X":
                vCount += 1
            elif position[j][i] == "O":
                vCount += 4

            # checks left diagonal
            if i == j:
                if position[i][j] == "X":
                    ldCount += 1
                elif position[i][j] == "O":
                    ldCount += 4

            if i == 2 - j:
                if position[i][j] == "X":
                    rdCount += 1
                elif position[i][j] == "O":
                    rdCount += 4

        # horizontal analysis
        value += evaluate_count(hCount)

        # vertical analysis
        value += evaluate_count(vCount)
    
    # left diagonal analysis
    value += evaluate_count(ldCount)

    # right diagonal analysis
    value += evaluate_count(rdCount)

    return value

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
    
    x,y = raw_input("Move: ").split()
    board[int(y)][int(x)] = "X"
    print_board(board)
    move = minimax(board, 10, True)
    print_board(move)

main()
