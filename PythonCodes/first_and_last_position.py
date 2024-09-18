# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/1394128643/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        else:
            result = []
            result.append(nums.index(target))
            nums.reverse()
            result.append(len(nums)-nums.index(target)-1)
            
        return result
            
        