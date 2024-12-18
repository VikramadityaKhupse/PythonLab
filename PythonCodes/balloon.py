# https://leetcode.com/problems/maximum-number-of-balloons/submissions/1420182286/
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for char in text:
            if char in counts:
                counts[char] += 1

        counts['l'] //= 2
        counts['o'] //= 2
        
        
        return min(counts.values())
