# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  
        max_profit = 0  
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                if (price - min_price) > max_profit:
                    max_profit = (price - min_price)
        
        return max_profit
