# https://leetcode.com/problems/multiply-strings/submissions/1397661034/
class Solution:
    def str_to_int(self, char):
        return ord(char) - 48  
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                mul = self.str_to_int(num1[i]) * self.str_to_int(num2[j])
                result[i + j] += mul

                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(map(str, result[::-1]))


