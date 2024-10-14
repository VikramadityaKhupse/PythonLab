import random
def create_grid(rows, cols):

    dynamic_grid = []
    for row in range(rows):
        dynamic_grid.append(dict().fromkeys(range(0, cols ), " "))
    return dynamic_grid

def print_grid(grid):
    col_len = len(grid)
    
    print("\n")
    print("___ " * col_len)
    for row in grid:
        print("|".join(f" {row[col]} " for col in range(0, col_len )) + "|")
        print("___ " * col_len)
    print("\n")




def fill_sudoku(grid, size):
	p = set(range(1, size+1))
	for row in range(size):
		for col in range(size):
			avail = set(list(grid[row].values()) + [r.get(col) for r in grid])
			candi = list(p-avail)
			grid[row][col] = candi[random.randint(0, len(candi)-1)]
	print_grid(grid)




def initialize():
	print("\t\tWelcome to sudoku!!")
	
	size = int(input("Enter size of grid: "))
	grid = create_grid(size, size)
	
	fill_sudoku(grid, size)
    
	



def sudoku():
	initialize()

sudoku()

