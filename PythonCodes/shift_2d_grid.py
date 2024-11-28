# https://leetcode.com/problems/shift-2d-grid/description/
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        flat_grid = [grid[i][j] for i in range(m) for j in range(n)]
        
        k %= total_elements
        flat_grid = flat_grid[-k:] + flat_grid[:-k]
        
        return [flat_grid[i * n:(i + 1) * n] for i in range(m)]
