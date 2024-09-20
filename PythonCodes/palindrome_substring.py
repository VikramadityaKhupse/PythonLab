# https://leetcode.com/problems/palindromic-substrings/description/
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        result = 0
        for i in range(len(s)):
            result += expandAroundCenter(i, i)   
            result += expandAroundCenter(i, i+1) 
        
        return result
