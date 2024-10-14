def create_grid(rows, cols):

    dynamic_grid = []
    for row in range(rows):
        dynamic_grid.append(dict().fromkeys(range(1, cols + 1), " "))
    return dynamic_grid

def print_grid(grid):
    col_len = len(grid)
    print("\n")
    print(" _ " * col_len)
    for row in grid:
        print("| ".join(f"{row[col]}" for col in range(1, col_len + 1)) + "|")
        print(" _ " * col_len)
    print("\n")


def is_valid_move(grid, row, col, num):

    for i in range(1, 10):
        if grid[row][i] == num or grid[i][col] == num:
            return False


    subgrid_row_start = ((row - 1) // 3) * 3 + 1
    subgrid_col_start = ((col - 1) // 3) * 3 + 1
    for r in range(subgrid_row_start, subgrid_row_start + 3):
        for c in range(subgrid_col_start, subgrid_col_start + 3):
            if grid[r][c] == num:
                return False
    return True


def start_game():

    grid = create_grid(9, 9)
    

    grid[1][1] = 5
    grid[2][2] = 3
    grid[3][3] = 7
    print("Welcome to Sudoku!")
    
    while True:
        print_grid(grid)
        

        row = int(input("Enter row (1-9): ")) -1 
        col = int(input("Enter column (1-9): ")) -1
        num = int(input("Enter number (1-9): "))
        

        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
        else:
            print("Invalid move. Try again.")
        

        if input("Continue? (y/n): ") != "y":
            break

start_game()

