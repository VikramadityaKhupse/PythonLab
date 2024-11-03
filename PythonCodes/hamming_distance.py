# https://leetcode.com/problems/hamming-distance/submissions/1441458988/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

        
            