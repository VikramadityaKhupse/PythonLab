# https://leetcode.com/problems/backspace-string-compare/description/
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processString(text: str) -> str:
            stack = []
            for char in text:
                if char == '#':
                    if stack:
                        stack.pop()  
                else:
                    stack.append(char)  
            return ''.join(stack)

        return processString(s) == processString(t)
