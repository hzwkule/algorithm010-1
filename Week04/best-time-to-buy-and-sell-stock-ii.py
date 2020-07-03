class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1,0,-1):
            if prices[i] > prices[i-1]:
                profit = profit + prices[i] - prices[i-1]
        return profit
                
