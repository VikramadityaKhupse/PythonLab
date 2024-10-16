# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        for num in nums:
            if nums.count(num) == n:
                return num 
        