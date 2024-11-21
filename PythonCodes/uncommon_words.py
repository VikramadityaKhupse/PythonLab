# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dict1 = {}
        
        for word in s1.split() + s2.split():
            dict1[word] = dict1.get(word, 0) + 1
        return [word for word in dict1.keys() if dict1[word] == 1]