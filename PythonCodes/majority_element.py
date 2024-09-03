# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        nums = sorted(nums)
        n = len(nums)
        curr_ele = nums[0]
        for i in range(n):
            if nums[i] == curr_ele:
                count += 1
            else:
                curr_ele = nums[i]
            if count > (n/2):
                return nums[i]
            

            
        