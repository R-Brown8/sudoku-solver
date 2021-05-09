"""
Ryan Brown
Sodoku Solver created using a backtracing algorithm
"""

board  = [
    [0,8,0,6,0,0,0,0,0],
    [6,0,0,0,7,0,0,2,0],
    [4,1,0,0,0,0,0,8,9],
    [0,7,0,9,0,0,0,0,4],
    [0,0,0,3,5,2,9,0,0],
    [0,0,5,0,0,0,1,6,0],
    [0,0,0,0,0,5,0,0,3],
    [9,0,6,1,0,0,0,4,0],
    [8,0,3,0,0,7,2,0,0]
]

def print_board(board):

     for i in range(len(board)):
         if i % 3 == 0 and i != 0:
            print( "- - - - - - - - - - - -")

         for j in range(len(board[0])):
             if j % 3 == 0 and j != 0:
                 print(" | ", end="")

             if j == 8:
                print(board[i][j])
             else:
                print(str(board[i][j]) + " ", end="")

def find_empty_squares(board):
    """
    Loop through the board and find position where there is empty square (0 = empty) and return position
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)  #row , column

    #if there are no blank squres
    return None

def valid_square(board, number, position):
    # check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check column
    for i in range(len(board[0])):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    # if made to end of checks
    return True

def solve(board):

    find = find_empty_squares(board)
    if not find:
         return True
    else:
        row, col = find

    for i in range(1,10):
        if valid_square(board, i, (row,col)):
            board[row][col] = i

            if solve(board):
                return True

            #if not possible backtrack and reset last value
            board[row][col] = 0
    return False

print_board(board)
solve(board)
print("_______________________")
print("\n    Solved Board: \n")
print_board(board)