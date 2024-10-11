# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution:
    def uniqueOccurrences(self, arr):
        freq_dict = {}
        for num in arr:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        freq_set = set(freq_dict.values())
        
        return len(freq_set) == len(freq_dict)

        
        