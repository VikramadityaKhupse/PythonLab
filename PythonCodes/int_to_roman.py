# https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1:'I', 4:'IV', 5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
        nums = list(dic.keys())[::-1]
        roman = ""
        for digit in nums:
            roman += dic[digit]*(num // digit)
            num %= digit
        
        return roman
    
    
    


        