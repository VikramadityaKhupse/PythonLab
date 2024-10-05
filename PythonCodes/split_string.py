# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        count = 0

        for char in s:
            r_count += (char == 'R')
            l_count += (char == 'L')

            if r_count == l_count:
                r_count = 0
                l_count = 0
                count += 1
        return count
