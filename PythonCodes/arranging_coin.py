# https://leetcode.com/problems/arranging-coins/
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        for i in range(1,n+1):
            if i > n:
                break
            else:
                n -= i
                count += 1
        return count