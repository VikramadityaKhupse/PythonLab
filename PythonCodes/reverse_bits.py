# https://leetcode.com/problems/reverse-bits/description/
class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        for i in range(32):
        # Shift reversed_num to the left by 1 to make space for the next bit
            reversed_num <<= 1
        # Extract the least significant bit of n and add it to reversed_num
            reversed_num |= (n & 1)
        # Shift n to the right by 1 to process the next bit
            n >>= 1
        return reversed_num

        