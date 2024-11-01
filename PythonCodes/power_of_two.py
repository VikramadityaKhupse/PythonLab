# https://leetcode.com/problems/power-of-two/submissions/1439551024/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
         return n > 0 and str(bin(n)).count('1') == 1
