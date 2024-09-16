# https://leetcode.com/problems/pascals-triangle/
from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        child_list = []
        for i in range(numRows):
            for j in range(i+1):
                child_list.append(factorial(i)//(factorial(j)*factorial(abs(i-j))))
            result.append(child_list)
            child_list = []
        return result
             
            


        