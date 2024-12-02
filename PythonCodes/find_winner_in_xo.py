# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [['' for _ in range(3)] for _ in range(3)]

        for i, (row, col) in enumerate(moves):
            player = 'X' if i % 2 == 0 else 'O'
            grid[row][col] = player

        def check_winner(player):
            for i in range(3):
                if all(grid[i][j] == player for j in range(3)):  
                    return True
                if all(grid[j][i] == player for j in range(3)):  
                    return True
            if all(grid[i][i] == player for i in range(3)):  
                return True
            if all(grid[i][2 - i] == player for i in range(3)):  
                return True
            return False

        if check_winner('X'):
            return "A"
        if check_winner('O'):
            return "B"

        if len(moves) == 9:  
            return "Draw"
        else:  
            return "Pending"