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


# function evaluates the current position
def evaluate(position):
    e = 0 # position value
    for i in range(3):
        h_xCount = 0 # horizontal count
        h_oCount = 0
        v_xCount = 0 # vertical count
        v_oCount = 0
        for j in range(3):
            # checks horizontal
            if position[i][j] == "X":
                h_xCount += 1
            elif position[i][j] == "O":
                h_oCount += 1

            if position[j][i] == "X":
                v_xCount += 1
            elif position[j][i] == "O":
                v_oCount += 1

        # horizontal analysis X
        if h_oCount == 0: # row must only consist of X values
            if h_xCount == 3: # 3 in a row
                e -= 100
            elif h_xCount == 2: # 2 in a row
                e -= 10
            elif h_xCount == 1: # 1 in a row
                e -= 1
        # horizontal analysis O
        elif h_xCount == 0:
            if h_oCount == 3:
                e += 100
            elif h_oCount == 2:
                e += 10
            elif h_oCount == 1:
                e += 1

        # vertical analysis X
        if v_oCount == 0: # col must only consist of X values
            if v_xCount == 3: # 3 in a col
                e -= 100
            elif v_xCount == 2: # 2 in a col
                e -= 10
            elif v_xCount == 1: # 1 in a col
                e -= 1
        # vertical analysis O
        elif v_xCount == 0:
            if v_oCount == 3:
                e += 100
            elif v_oCount == 2:
                e += 10
            elif v_oCount == 1:
                e += 1
    return e

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
                max_pos = pos
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
                min_pos = pos
        return min_pos

def main(): 
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    print_board(board)
    
    x,y = raw_input("Move: ").split()
    board[int(y)][int(x)] = "X"
    print_board(board)
    move = minimax(board, 3, True)
    print_board(move)

main()
