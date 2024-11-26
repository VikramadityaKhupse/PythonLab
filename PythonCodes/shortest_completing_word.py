# https://leetcode.com/problems/shortest-completing-word/description/
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        def get_letter_counts(s: str):
            counts = {}
            for char in s:
                if char.isalpha():  
                    char = char.lower()
                    counts[char] = counts.get(char, 0) + 1
            return counts

        license_counts = get_letter_counts(licensePlate)
        
        def can_complete(word: str, required_counts: dict) -> bool:
            word_counts = {}
            for char in word:
                word_counts[char] = word_counts.get(char, 0) + 1
            
            for char, count in required_counts.items():
                if word_counts.get(char, 0) < count:
                    return False
            return True
        
        shortest_word = None
        for word in words:
            if can_complete(word, license_counts):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word
