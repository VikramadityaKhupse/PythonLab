# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            length = 0
            while num != 0:
                length += 1
                num //= 10
            count += length % 2 == 0
            length = 0
        return count