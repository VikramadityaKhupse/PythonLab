# https://leetcode.com/problems/add-digits/submissions/1387303666/
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10 and not None:
            return num
        else:
            new_list = map(int, list(str(num)))
            return self.addDigits(sum(new_list))
            

        