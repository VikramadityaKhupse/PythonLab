# https://leetcode.com/problems/factorial-trailing-zeroes/submissions/1398619302/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count

        


        

# class Solution:
#     def factorial(self, n):
#         if n == 0 or n == 1:
#             return 1
#         else:
#             return n * factorial(n - 1)

#     def trailingZeroes(self, n: int) -> int:
#         fact = self.factorial(n)
#         count = 0
#         for char in str(fact)[::-1]:
#             if char == '0':
#                 count += 1
#         return count

        


        