# https://leetcode.com/problems/smallest-range-i/submissions/1425603286/
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        
        max_num = max(nums)
        min_num = min(nums)
        
        min_score = (max_num - k) - (min_num + k)
        
        return max(0, min_score)