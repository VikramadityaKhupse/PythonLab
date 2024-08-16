# https://leetcode.com/problems/longest-common-prefix/submissions/1358092032/

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs = sorted(strs)

        string1 = strs[0]
        string2 = strs[-1]

        i = 0
        while i < len(string1) and i < len(string2) and string1[i] == string2[i]:
            i += 1
        
        return string1[:i]

        

        
        

        