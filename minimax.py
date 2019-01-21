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
    eval = 0
    for i in range(3):
        h_xCount = 0 # horizontal count
        h_oCount = 0
        v_xCount = 0 # vertical count
        v_oCount = 0
        for j in range(3):
            # checks horizontal
            if position[i][j] == "X":
                h_xCount +=1
            elif position[i][j] == "O":
                h_oCount += 1

            if position[j][i] == "X":
                v_xCount += 1
            elif position[j][i] == "O":
                v_oCount += 1

        # horizontal analysis X
        if h_oCount == 0: # row must only consist of X values
            if h_xCount == 3: # 3 in a row
                eval += 100
            elif h_xCount == 2: # 2 in a row
                eval += 10
            elif h_xCount == 1: # 1 in a row
                eval += 1
        # horizontal analysis O
        elif h_xCount == 0:
            if h_oCount == 3:
                eval -= 100
            elif h_oCount == 2:
                eval -= 10
            elif h_oCount == 1:
                eval -= 1

        # vertical analysis X
        if v_oCount == 0: # col must only consist of X values
            if v_xCount == 3: # 3 in a col
                eval += 100
            elif v_xCount == 2: # 2 in a col
                eval += 10
            elif v_xCount == 1: # 1 in a col
                eval += 1
        # vertical analysis O
        elif v_xCount == 0:
            if v_oCount == 3:
                eval -= 100
            elif v_oCount == 2:
                eval -= 10
            elif v_oCount == 1:
                eval -= 1
    return eval

def get_children(position, player):
    #TODO
    return position

# function calculates a specified number of moves ahead (depth) 
# to predict the best move
def minimax(position, depth, max_player):

    if depth == 0 or game_over(position):
        return evaluate(position)

    if max_player:
        max_eval = -1 * inf
        children = get_children(position, max_player)
        for child in children:
            evaluation = minimax(child, depth-1, false)
            # compares the current evaluation to the one calculated
            max_eval = max(max_eval, evaluation)
        return max_eval

    else:
        min_eval = inf
        children = get_children(poition, max_player)
        for child in children:
            evaluation = minimax(child, depth-1, true)
            # compares the current evaluation to the one calculated
            min_eval = min(min_eval, evaluation)
        return minEval


def main(): 
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    print_board(board)
    
    while not game_over(board):
        x,y = raw_input("Move: ").split()
        board[int(y)][int(x)] = "X"
        print_board(board)
        print("Eval: " + str(evaluate(board)))

main()
