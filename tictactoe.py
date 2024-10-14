def create_grid(rows, col):
    dynamic_grid = []
    for row in range(rows):
        dynamic_grid.append(dict().fromkeys(range(1, col + 1), " "))
    return dynamic_grid


def print_grid(grid):
    col = len(grid)
    print("\n")
    print("__ " * col)
    for row in grid:
        print("| ".join(f"{row[col]}" for col in range(1, col + 1)) + "|")
        print( "__ " * col)
    print("\n")


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


def is_full(grid):
    for row in grid:
        if " " in row.values():
            return False
    return True


def play_move(grid, player, pos):
    row, col = pos
    if grid[row - 1][col] == " ":
        grid[row - 1][col] = player
        return True
    return False


def start_game():
    grid = create_grid(3, 3)
    player_turn = "X"
    
    while True:
        print_grid(grid)
        print(f"Player {player_turn}, it's your turn.")
        
        try:
            pos_x = int(input("Enter the row (1-3): "))
            pos_y = int(input("Enter the column (1-3): "))
        except ValueError:
            print("Invalid input! Please enter numbers between 1 and 3.")
            continue

        if not (1 <= pos_x <= 3 and 1 <= pos_y <= 3):
            print("Invalid position! Please enter a valid position (1-3).")
            continue

        if not play_move(grid, player_turn, (pos_x, pos_y)):
            print("This position is already taken! Try again.")
            continue

        winner = check_winner(grid)
        if winner:
            print_grid(grid)
            print(f"Player {winner} wins!")
            break

        if is_full(grid):
            print_grid(grid)
            print("It's a draw!")
            break

        player_turn = "O" if player_turn == "X" else "X"


start_game()
