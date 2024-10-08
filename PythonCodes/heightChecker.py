# https://leetcode.com/problems/height-checker/solutions/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0

        for index, num in enumerate(expected):
            if heights[index] != num:
                count += 1
        return count