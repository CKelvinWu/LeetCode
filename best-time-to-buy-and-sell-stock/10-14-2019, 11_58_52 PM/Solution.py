// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        for i in range(len(prices)):
            
            for j in range(i + 1, len(prices)):
                if prices[i] <prices[j]:
                    profit = max(profit, prices[j] - prices[i])
                else:
                    break
                
        return profit