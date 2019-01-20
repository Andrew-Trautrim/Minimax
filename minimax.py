#!/usr/bin/python

def print_board(board):
    for i in board:
        row = ""
        for j in i:
            row += (j + " ")
        print(row)

def main():
    board = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    print_board(board)



main()
