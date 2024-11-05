# https://leetcode.com/problems/third-maximum-number/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        for num in set(nums):  
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
                
        return third if third != float('-inf') else first
