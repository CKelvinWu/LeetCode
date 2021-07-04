// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit, min_price = 0, float("inf")
        for i in prices:
            min_price = min(min_price, i)
            profit = max(profit, i - min_price)            
        return profit
        
        
        # profit = 0        
        # for i in range(len(prices)):            
        #     for j in range(i + 1, len(prices)):
        #         if prices[i] < prices[j]:
        #             profit = max(profit, prices[j] - prices[i])
        #         else:
        #             break  
        # return profit