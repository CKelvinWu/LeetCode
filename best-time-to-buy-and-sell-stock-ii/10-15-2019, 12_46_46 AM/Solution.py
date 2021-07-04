// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit, min_price, local_max = 0, float("inf"), 0
        
        for i in range(len(prices) - 1):
            min_price = min(min_price, prices[i])
            local_max = max(local_max, prices[i] - min_price)
            if prices[i+1] - prices[i] < 0:
                profit += local_max
                min_price, local_max = float("inf"), 0                
            elif prices[i+1] - prices[i] >= 0 and i == len(prices) - 2:
                profit += max(local_max, prices[i+1] - min_price)
            
            
                
        return profit