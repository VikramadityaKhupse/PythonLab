# https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = num[::-1]
        
        k_list = [int(x) for x in str(k)][::-1]
        
        result = []
        carry = 0
        max_len = max(len(num), len(k_list))

        for i in range(max_len):
            digit_num = num[i] if i < len(num) else 0
            digit_k = k_list[i] if i < len(k_list) else 0
            
            total = digit_num + digit_k + carry
            
            carry = total // 10
            
            result.append(total % 10)

        if carry:
            result.append(carry)

        return result[::-1]
