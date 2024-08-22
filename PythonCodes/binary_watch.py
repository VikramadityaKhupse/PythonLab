# https://leetcode.com/problems/number-complement/submissions/1364740908/?envType=daily-question&envId=2024-08-22
class Solution:
    def findComplement(self, num: int) -> int:
        bin_list = list(bin(num)[2:])
        for i,char in enumerate(bin_list):
            if char == '1':
                bin_list[i] = '0'
            else:
                bin_list[i] = '1'
        return int("".join(bin_list), 2)
        
        