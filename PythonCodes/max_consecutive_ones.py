# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = current_count = 0
        
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = current_count if current_count > max_count else max_count
            else:
                current_count = 0  
        return max_count

# OR
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max("".join(map(str, nums)).split('0')))
