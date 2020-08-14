board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# This function will print the board to the terminal
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="")


# This function will find an empty position in the board

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row, column

    # Return none if no empty square found
    return None

# This function will check if a position in the board is valid (unique by rows, columns and sub boards)
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3   # Position of box in the horizontal axis
    box_y = pos[0] // 3   # Position of box in the vertical axis

    for i in range(box_y * 3 , box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True

# Main function applying backtracking algorithm 
def solve(bo):
    find = find_empty(bo)
    if not find: # If all the squares have been filled
        return True
    else:
        row, col = find

    # This for loop indeed is the backtracking algorithms
    # which use recursion to solve the problem :)))
    for val in range(1, 10):
        if valid(bo, val, (row, col)):
            bo[row][col] = val 

            if solve(bo):
                return True
            
            bo[row][col] = 0
    
    return False


solve(board)
print_board(board)
