def create_grid(rows, col):
	#grid = [{1:"1",2:"2",3:"3"},
	#{1:"1",2:"2",3:"3"},{1:"1",2:"2",3:"3"}]
	
	dynamic_grid = []
	for row in range(rows):
		dynamic_grid.append(dict().fromkeys(range(1,col+1), " " ))
	
	return dynamic_grid


def print_grid(num, pos, grid):
	col = len(grid)
	pos_x, pos_y = pos
	grid[pos_x-1][pos_y-1] = num
	print(" "+" ___" * (col-1))
	for row in grid:
		print("|  ".join(f"{row[col]}" for col in range(1,col+1))+"|")
		
		print(" "+" ___" * (col-1))

def check_winner(grid):
    for i in range(3):
        if grid[i][1] == grid[i][2] == grid[i][3] != " ":
            return grid[i][1]
        if grid[0][i + 1] == grid[1][i + 1] == grid[2][i + 1] != " ":
            return grid[0][i + 1]

    if grid[0][1] == grid[1][2] == grid[2][3] != " ":
        return grid[0][1]
    if grid[0][3] == grid[1][2] == grid[2][1] != " ":
        return grid[0][3]

    return None

def start_game():
	grid = create_grid(3, 3)
	
	print_grid("10",(1,2),grid)
	
	
start_game()
