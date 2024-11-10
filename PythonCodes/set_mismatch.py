# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set1 = set(nums)
        set2 = set(i for i in range(1, len(nums)+1))
        missing_num = sum(set2) - sum(set1)
        return [abs(sum(set2)- sum(nums)- missing_num), missing_num ]


            




