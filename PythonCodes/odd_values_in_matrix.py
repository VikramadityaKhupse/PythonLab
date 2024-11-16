# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]
        count = 0
        for index in indices:
            row_num, col = index
            for i in range(n):
                matrix[row_num][i] += 1
            for j in range(m):
                matrix[j][col] += 1

        for row in matrix:
            for num in row:
                if num % 2 != 0:
                    count += 1
        return count