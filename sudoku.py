import random

def create_grid(rows, cols):
    # Create a grid using a list of dictionaries for each row
    return [dict((col, " ") for col in range(cols)) for _ in range(rows)]

def print_grid(grid):
    size = len(grid)
    print("\n")
    print(" ___" * size)
    for row in grid:
        print("|" + "|".join(f" {row[col]} " for col in row) + "|")  # Corrected here
        print(" ___" * size)
    print("\n")


def fill_sudoku(grid, size):
    # Set of possible numbers in Sudoku
    numbers = set(range(1, size+1))
    
    for row in range(size):
        for col in range(size):
            # Get current row and column values
            row_values = set(grid[row].values())
            col_values = set(grid[r][col] for r in range(size))
            
            # Calculate available candidates for the cell
            available = numbers - (row_values | col_values)
            
            if available:
                grid[row][col] = random.choice(list(available))
    
    print_grid(grid)

def initialize():
    print("\t\tWelcome to Sudoku!!")
    
    # Asking user for grid size (e.g., 9x9)
    size = int(input("Enter size of grid (e.g., 9 for 9x9): "))
    
    # Create an empty grid
    grid = create_grid(size, size)
    
    # Fill and print the Sudoku grid
    fill_sudoku(grid, size)

def sudoku():
    initialize()

# Start Sudoku
sudoku()
