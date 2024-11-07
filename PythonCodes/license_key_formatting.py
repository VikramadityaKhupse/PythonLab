# https://leetcode.com/problems/license-key-formatting/description/
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        grouped_list = [s[max(i - k, 0):i] for i in range(len(s), 0, -k)]
        
        return "-".join(grouped_list[::-1])
