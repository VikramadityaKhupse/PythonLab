# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        
        x_string = str(abs(x))[::-1]
        
        reversed_number = int(x_string)
        
        if is_negative:
            reversed_number = -reversed_number
        
        if reversed_number < -2**31 or reversed_number > 2**31 - 1:
            return 0
        
        return reversed_number
