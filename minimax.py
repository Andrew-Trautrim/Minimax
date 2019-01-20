#!/usr/bin/python
inf = 999 # infinity

# displays current bard position
def print_board(board):
    for i in board:
        row = ""
        for j in i:
            row += (j + " ")
        print(row)

# utility function, determines if the game has been finished
def game_over(board):
    #TODO
    count = 0;
    for i in board:
        for j in i:
            if j == "X":
                count++
            elif j == "O":
                count--
        if(count == 3 or count == -3):
            return True

#function evaluates the current position and rates it
def evaluate(position):
    # TODO

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
    
    for i in range(9):
        x,y = raw_input("Move: ").split()
        board[int(y)][int(x)] = "X"
        print
        print_board(board)

main()
