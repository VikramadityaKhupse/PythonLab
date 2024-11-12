# https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join([word for word in s.split()[::-1]])