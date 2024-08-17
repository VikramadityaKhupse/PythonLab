# https://leetcode.com/problems/valid-parentheses/submissions/1359357530/
class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")":"(","}":"{","]":"["}
        stack = []
        
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                if stack and stack[-1] == dictionary[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return not stack
