# https://leetcode.com/problems/baseball-game/description/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            try:
                stack.append(int(operation))
            except ValueError:
                if operation == '+':
                    stack.append(stack[-1] + stack[-2])
                elif operation == 'D':
                    stack.append(stack[-1] * 2)
                elif operation == 'C':
                    stack.pop()

        return sum(stack)
