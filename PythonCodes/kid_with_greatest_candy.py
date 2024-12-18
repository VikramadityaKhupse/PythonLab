# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        

        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max_candies)
        
        return result

        