# https://leetcode.com/problems/roman-to-integer


class Solution:
    def romanToInt(self, s: str) -> int:
        map1 = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        output = 0
        last_num = None
        for char in s:
            if(last_num is not None and last_num < map1[char]):
                output -= last_num
                output += (map1[char] - last_num)
                last_num = map1[char]
            else:
                output+= map1[char]
                last_num = map1[char]
            
        return output

            
        

