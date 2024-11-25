# https://leetcode.com/problems/self-dividing-numbers/description/
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            n = i
            while n != 0:
                digit = n % 10
                if (digit == 0) or i % (n % 10) != 0:
                    break
                else:
                    n //= 10
            else:
                result.append(i)
        return result