# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1392906608/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits:
            return []

        result = num_to_char_dict[digits[0]]

        for digit in digits[1:]:
            if digit in num_to_char_dict:
                result = [prev + curr for prev in result for curr in num_to_char_dict[digit]]

        return result


