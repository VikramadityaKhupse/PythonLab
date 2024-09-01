# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = [char for char in s.lower() if char.isalnum()]
        
        return l == l[::-1]
        