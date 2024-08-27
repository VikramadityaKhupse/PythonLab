# https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return map(int,list(str(int(str(''.join(map(str, digits))))+1)))
        